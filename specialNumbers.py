print("-----------------------------------------------------------------------------")
print("                                SPECIAL NUMBERS                              ")
print("-----------------------------------------------------------------------------")

try:
    num1 = int(input("\nEnter a number: "))
    num2 = int(input("Enter another number: "))

    print(f"\nInput 1 = {num1}")
    print(f"Input 2 = {num2}")

    print("Special Numbers:  \n\t")

    #Special numbers are those divisible to input without a remainder.
    #range 1-50.
    for i in range(1,51):
        #print(i)
        if i % num1 == 0 :
            print("\t" + str(i),end=",")

        elif i % num2 == 0:
            print("\t"+str(i), end=",")

except ValueError as err:
    print(f"\tERROR : {err}")

finally:
    print("\n\n-----------------------------------------------------------------------------")

