from cryptography.fernet import Fernet # Capital F for the class

message = "Hello User!"
print(f"Original: {message}")

# 1. Generate the key
key = Fernet.generate_key()

# 2. Rename the variable to 'cipher_suite' to avoid overwriting the module
cipher_suite = Fernet(key)

# 3. Encrypt
encrypted = cipher_suite.encrypt(message.encode())
print(f"Encrypted: {encrypted}")

# 4. Decrypt
decrypted = cipher_suite.decrypt(encrypted).decode()
print(f"Decrypted: {decrypted}")