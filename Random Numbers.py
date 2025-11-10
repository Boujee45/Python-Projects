import random

#random.randint(range)
print(f"Random number: {random.randint(0,200)}")
print(f"Random number: {random.randint(0,200)}")
print(f"Random number: {random.randint(0,200)}")
print(f"Random number: {random.randint(0,200)}")

#print(help(random))

number = random.random()#floating point random

print(number)

options = ("rock","paper","scissors")

print(random.choice(options))#sequence random

cards =["2","3","4","5","6","7","8","9","10","J","k","Q","A"]

random.shuffle(cards)

print(cards)