#Concession Stand Program


menu = {"pizza" : 3.00,
        "nachos" : 4.50,
        "popcorn" : 6.00,
        "fries" : 2.50,
        "chips" : 1.00,
        "pretzel" : 3.50,
        "soda" : 3.00,
        "lemonade" : 4.25
        }

total = 0
cart = []

print("------------MENU------------")

for key,value in menu.items():
    print(f"{key:10}: ${value:.2f}")

print("----------------------------\n")

while True:
    food = input("Select a food item(q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("\n---------YOUR ORDER---------\n")

for food in cart:
    total += menu.get(food)
    print(food,end=" ")

print()
print(f"\nTotal is: ${total:.2f}")

print(f"\t\t= ${total:.2f}")

print("----------------------------")