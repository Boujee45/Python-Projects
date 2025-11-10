import cmath

try:
        print("-----------------------------------------------------")
        print("                    CALCULATOR                       ")
        print("-----------------------------------------------------")

        num1 = float(input("\nEnter a number: "))
        num2 = float(input("Enter another number: "))

        print("\nOperators include: ")
        print("\t+ : Addition")
        print("\t- : Substraction")
        print("\t* : Multiplication")
        print("\t/ : Division")

        operator = input("Enter an operator: ")


        '''print(f"\nNum1 = {num1}")
        print(f"Num2 = {num2}")
        print(f"\nSolution = {num1} {operator} {num2} ")'''

        if operator == "+":
            print(f"\nNum1 = {num1}")
            print(f"Num2 = {num2}")
            print(f"\nSolution = {num1} {operator} {num2} ")
            print("\t\t\t\tAns = " + str(num1 + num2))
        elif operator == "-":
            print(f"\nNum1 = {num1}")
            print(f"Num2 = {num2}")
            print(f"\nSolution = {num1} {operator} {num2} ")
            print("\t\t\t\tAns = " + str(num1 - num2))
        elif operator == "*":
            print(f"\nNum1 = {num1}")
            print(f"Num2 = {num2}")
            print(f"\nSolution = {num1} {operator} {num2} ")
            print("\t\t\t\tAns = " + str(num1 * num2))
        elif operator == "/":
            print(f"\nNum1 = {num1}")
            print(f"Num2 = {num2}")
            print(f"\nSolution = {num1} {operator} {num2} ")
            print("\t\t\t\tAns = " + str(num1 / num2))
        else:
            print(f"\nERROR : INVALID INPUT! - {"'" + operator + "'"}")


except ZeroDivisionError as err:
    print(err)
except ValueError as err:
    print(err)

finally:
    print("\n                  THANK YOU , BYE!                   ")
    print("-----------------------------------------------------")
