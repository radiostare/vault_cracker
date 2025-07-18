import base64
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Hash import SHA256

# --- Your Provided Data ---
pbkdf2_salt_b64 = "enter value"
symmetric_key_b64 = "enter value"
hashed_key_b64 = "enter value"

pbkdf2_salt = base64.b64decode(pbkdf2_salt_b64)
symmetric_key = base64.b64decode(symmetric_key_b64)
stored_hash = hashed_key_b64.strip()

# Parse IV and ciphertext—ignore tag entirely
iv = symmetric_key[2:14]            # 12 bytes
cipher_text = symmetric_key[14:46]  # 32 bytes
# tag = symmetric_key[46:]          # DROPPED—no longer used

ITERATIONS = 4096

def sha256_b64(data):
    return base64.b64encode(SHA256.new(data).digest()).decode('ascii').rstrip('=')

def attempt_pin(pin, keylen):
    # Derive primary key
    primary = PBKDF2(pin, pbkdf2_salt, dkLen=keylen, count=ITERATIONS, hmac_hash_module=SHA256)
    # Decrypt WITHOUT verifying tag
    cipher = AES.new(primary, AES.MODE_GCM, nonce=iv)
    master_key = cipher.decrypt(cipher_text)
    # Compare SHA256(master_key) as base64
    if sha256_b64(master_key) == stored_hash.rstrip('='):
        print(f"✅ PIN found: {pin} (key length: {keylen * 8} bits)")
        return True
    return False

# Brute-force all 4-digit PINs (1000–9999) for key lengths 256 & 128 bits
for pin_int in range(1000, 10000):
    pin = str(pin_int)
    for k in (32, 16):
        if attempt_pin(pin, k):
            exit()
    if pin_int % 1000 == 0:
        print(f"Tried up to {pin}")

print("❌ Failed to find PIN. Check keylen assumptions or iteration count.")

