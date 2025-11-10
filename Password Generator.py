import random
import string

def generate_password(length = 12):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = string.digits
    symbols = string.punctuation #"!@#$%^&*()?<>|{}[],~`,/"

    all_chars = lowercase + uppercase + numbers + symbols

    password = ''.join(random.choice(all_chars) for _ in range(length))

    return password

print("---------------------------------------------------------------------------")
print("                            PASSWORD GENERATOR                             ")
print("---------------------------------------------------------------------------")

for i in range(5):
    print(f"\n{i + 1}.{generate_password()}")

print("\n---------------------------------------------------------------------------")
