import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
#string.whitespace
#string.__all__ - all functions

chars = list(chars)
keys = chars.copy()

random.shuffle(keys)

#print(f"chars: {chars}")
#print(f"keys: {keys}")

#ENCRYPT
print("***************************************************")
print("              ENCRYPT AND DECRYPT                  ")
print("***************************************************")

plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += keys[index]

print(f"\nOriginal Message: {plain_text}")
print(f"Encrypted Message: {cipher_text}")


#DECRYPT

cipher_text = input("\nEnter a message to decrypt: ")
plain_text = ""

for letter in cipher_text:
    index = keys.index(letter)
    plain_text += chars[index]

print(f"\nEncrypted Message: {cipher_text}")
print(f"Original Message: {plain_text}")


print("***************************************************")