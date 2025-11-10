import math
from math import *

try:
    print("--------------------------------------------------------------------")
    print("                         TRIANGLE CALCULATOR                        ")
    print("--------------------------------------------------------------------")

    a = float(input("\nEnter a number for side a: "))
    b = float(input("Enter a number for side b: "))
    c = float(input("Enter a number for side c: "))

    #Area of Triangle  = (b + h)/2
    #s = (a + b + c)/2
    #Area of Triangle = (s*(s-a)*(s-b)*(s-c)) ** 0.5

    p = a + b + c

    s = p / 2

    #A =(s * (s - a)*(s - b) * (s - c)) ** 0.5
    A = math.sqrt((s * (s - a) * (s - b) * (s - c)))

    print(f"\nInput a = {a}")
    print(f"Input b = {b}")
    print(f"Input c = {c}")

    print(f"\t\tPerimeter = {p}cm")
    print(f"\t\tArea  =  {A : .3}cm^2")

except ValueError as err:
    print(err)
finally:
    print("\n                         THANK YOU , BYE                          ")
    print("--------------------------------------------------------------------")
