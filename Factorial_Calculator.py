try:
    print("--------------------------------------------------------------------")
    print("                       FACTORIAL CALCULATOR                         ")
    print("--------------------------------------------------------------------")

    Explanation = ""
    num = int(input("\nEnter a number for the factorial: "))
    factorial = 1

    if num < 0:
        print(f"\nInput = {num}")
        print("\tERROR : There is no factorial for a negative number!")

    elif num == 0 or num == 1:
        print(f"\nInput = {num}")
        print("Factorial = 1")
        print(f"\t\t\tAns = {factorial}")

    else:
        for i in range(1,num + 1):
            factorial *= i
            Explanation += str(i)

            if i < num:
                Explanation += " x "

        print(f"\nInput = {num}")
        print(f"Factorial = {Explanation}")
        print(f"\t\t\tAns = {factorial}")

except ValueError as err:
    print(f"\n\tERROR : {err}")

finally:
    print("\n                        THANK YOU , BYE!                          ")
    print("--------------------------------------------------------------------")
