import random
import string


def generate_pin(length = 4):

    numbers = string.digits

    pin = ''.join(random.choice(numbers) for _ in range(length))
    
    return pin

print("==========================================================================")
print("                            PIN GENERATOR                                 ")
print("==========================================================================")

for i in range(5):
    print(f"{i + 1}. {generate_pin()}")

print("==========================================================================")
