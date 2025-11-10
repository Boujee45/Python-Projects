import cmath
import math

#x = (-b +- (b^2 - 4ac))/2a
try:
    print("----------------------------------------------------------")
    print("              QUADRATIC EQUATION CALCULATOR               ")
    print("----------------------------------------------------------")

    a = float(input("Enter a number for a: "))
    b = float(input("Enter a number for b: "))
    c = float(input("Enter a number for c: "))

    #d = b^2 - 4ac

    d = pow(b,2) - (4 * a * c)

    #x1 = -b - (cmath.sqrt(d))/2a

    x1 = (-b - cmath.sqrt(d))/2 * a

    #x2 = (-b + (cmath.sqrt(d))/2a

    x2 = (-b + cmath.sqrt(d))/2 * a

    print(f"\nInput a = {a}")
    print(f"Input b = {b}")
    print(f"Input c = {c}")

    print(f"\n\t\t x1 = {x1}")

    print(f"\t\t x2 = {x2}")
except ValueError as err:
    print(f"\tERROR : {err}")

finally:
    print("\n                      THANK YOU , BYE!                    ")
    print("----------------------------------------------------------")
