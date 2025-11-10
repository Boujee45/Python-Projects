try:
    print("-----------------------------------------------------------------")
    print("                         PRIME NUMBERS APP                       ")
    print("-----------------------------------------------------------------")

    num = int(input("Enter a number: "))

    if num > 1:
        for i in range(2,num):
            if (num % i ) == 0:
                print(f"\nSol = {i} x {num // i} = {num}")
                print(f"\n\t~ {num} is not a prime number")
                break

        else:
                print(f"\n\t~ {num} is a prime number.")

    else:
        print(f"\n\t~ {num} is not a prime number.")

except ValueError as err:
    print(f"\tERROR : {err}")

finally:
    print("\n                      THANK YOU , BYE!                         ")
    print("-----------------------------------------------------------------")
