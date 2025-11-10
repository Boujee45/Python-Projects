try:
    print("--------------------------------------------------------")
    print("                    NUMBER CHECKER                      ")
    print("--------------------------------------------------------")

    num = float(input("\nEnter a number: "))

    if num < 0:
        print("The number is a negative number.")
    elif num == 0:
        print("The number is zero")
    else:
        print("The number is a positive number.")
except ValueError as err:
    print(f"\n\tERROR : {err}")

finally:
    print("\n                   THANK YOU , BYE                    ")
    print("--------------------------------------------------------")
