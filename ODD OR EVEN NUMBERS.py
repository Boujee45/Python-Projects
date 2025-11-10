from math import remainder
try:
    print("-------------------------------------------------")
    print("            ODD AND EVEN NUMBERS APP             ")
    print("-------------------------------------------------")

    num = float(input("Enter a number: "))

    if num % 2 == 0:
        print(f"\n\t~ {num} is an EVEN NUMBER")
    else:
        print(f"\n\t~ {num} is an ODD NUMBER")
except ValueError as err:
    print(f"\tERROR : {err}")

finally:
    print("\n                THANK YOU , BYE!                 ")
    print("-------------------------------------------------")
