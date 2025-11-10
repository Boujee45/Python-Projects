print("-----------------------------------------------------")
print("                 SWAPPING APP                        ")
print("-----------------------------------------------------")

try:


    a = float(input("Enter a number a: "))
    b =float(input("Enter another number b: "))

    print(f"\nValues before swapping: \n a = {a} \n b = {b}")


    '''temp = a
    a = b
    b = temp'''
    '''c = a
    a = b
    b = c'''

    a , b = b , a

    print(f"\nValues after swapping: \n a = {a} \n b = {b}")
except ValueError  as err:
    print(f"\tERROR : {err}")
finally:
    print("\n                THANK YOU , BYE!                   ")
    print("-----------------------------------------------------")
