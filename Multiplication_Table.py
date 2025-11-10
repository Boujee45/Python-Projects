print("---------------------------------------------------------")
print("                   MULTIPLICATION-TABLE                  ")
print("---------------------------------------------------------")

num = int(input("Enter a number for the multiplication table: "))

for i in range(1,100):
    print(f"{num} x {i} = {num * i}")
