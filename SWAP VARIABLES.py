print("-----------------------------------------------------")
print("                 SWAPPING APP                        ")
print("-----------------------------------------------------")

try:
    x = int(input("Enter a number x: "))
    y= int(input("Enter a number y: "))

    print(f"\nOriginal variables before swapping: \nx : {x}  \ny : {y}")

    temp = x
    x = y
    y = temp

    print(f"\nVariables after swapping are: \nx : {x}  \ny : {y}")
except ValueError as err:
   print(f"\tERROR : {err}")

finally:
    print("\n                THANK YOU , BYE!                   s")
    print("-----------------------------------------------------")





