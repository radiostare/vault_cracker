# vault_cracker
Secret Calculator Vault PIN cracker

This code will allow you to crack the PIN for secret calculator vault applications. These apps require a PIN (set by the user) followed by pressing the "=" sign to enter it. THen a secret vault of media can be opened, which would otherwise be encrypted at the file level. You will need the AppPreferences.xml file to obtain the required salt/keys for this process. Python3 with pyCryptodome are required.

Usage:
$ python3 vault_cracker.py

To crack the PIN for the Secret Calculator Vault app, I extracted key cryptographic values from the app’s preferences file and replicated its authentication process in Python. For each possible 4-digit PIN, I derived a cryptographic key using PBKDF2 with the stored salt, then used that key to decrypt the app’s encrypted master key with AES-GCM (ignoring the authentication tag). I hashed the decrypted result with SHA256, base64-encoded it, and compared it to the stored hash value. When a match was found, the correct PIN was revealed, demonstrating how simple PINs can be brute-forced even when strong cryptography is used.

IF YOUR CASE INVOLVED A 4 DIGIT PIN, THE FOLLOWING SCRIPT WILL WORK.
IF NOT, EDIT THE VALUES ACCORDINGLY.

MAKE SURE YOU ENTER THE SALT, SYMMETRIC KEY AND HASHED KEY IN THE "ENTER VALUE" FIELD BEFORE RUNNING.

SOME DEPENDANCIES ARE REQUIRED FIRST.

=============================================================================

