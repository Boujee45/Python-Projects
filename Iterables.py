#Iterables : Collection that can return its elements one at a time allowing it to be iterated in a loop

#---Sets---
fruits = {"Apple","Banana","Oranges","Mangoes","StrawBerry"}

for fruit in fruits:
    print(fruit)

print()

#---List---

professions = ["Doctor","Teacher","Engineer","Mechanic","Hair Dresser"]

for profession in reversed(professions):
    print(profession)

print()

#---Dictionaries----
my_dictionary = {"A": 1,"B": 2,"C": 3,"D": 4,"E": 5}

for key,value in my_dictionary.items():
    print(f"{key}. {value}")

print()
#---Strings---
name = "Bad Boujee"

for character in name:
    print(character, end=" ")

print()
