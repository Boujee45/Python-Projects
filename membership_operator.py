#1. in
#2. not in

print()

word = "APPLE"

letter = input("Enter a letter in the secret word: ").upper()

if letter in word:
    print(f"{letter} is found in the word")
else:
    print(f"{letter} not found.")

print()

groceries = {"BANANAS","APPLES","ORANGES","TOMATOES","LEMON","CUCUMBERS"}

grocery_List = input("Enter the grocery you need: ").upper()

if grocery_List not in groceries:
    print(f"Sorry! we don't have {grocery_List} currently!")
else:
    print(f"{grocery_List} are available!")

print()

students = {"Patrick": "A", "Spongebob": "B", "Squidward": "C","Sandy": "D"}

name = input("Enter the student name: ").title()

if name in students:
    print(f"{name}'s grade is {students[name]}")
else:
    print(f"{name} not found!")

print()

email = "badboujee@gmail.com"

if "@" in email and "." in email:
    print("Valid Email!")

else:
    print("Invalid Email!")
