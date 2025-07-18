# vault_cracker
Secret Calculator Vault PIN cracker

To crack the PIN for the Secret Calculator Vault app, I extracted key cryptographic values from the app’s preferences file and replicated its authentication process in Python. For each possible 4-digit PIN, I derived a cryptographic key using PBKDF2 with the stored salt, then used that key to decrypt the app’s encrypted master key with AES-GCM (ignoring the authentication tag). I hashed the decrypted result with SHA256, base64-encoded it, and compared it to the stored hash value. When a match was found, the correct PIN was revealed, demonstrating how simple PINs can be brute-forced even when strong cryptography is used.
