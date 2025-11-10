try:

    print("-----------------------------------------------------------------------")
    print("                     COMPOUND INTEREST CALCULATOR                      ")
    print("-----------------------------------------------------------------------")


    Principle = 0
    rate = 0
    time = 0

    #
    while Principle <= 0:
        Principle = float(input("\nEnter the initial Principle Amount balance: "))
        if Principle < 0:
            print("\n\tThe Principal can't be less than or equal to 0!")

    while rate <= 0:
        rate = float(input("Enter the Interest rate: "))
        if rate <= 0:
            print("\n\tThe Interest rate can't be less than or equal to 0 %!")

    while time <= 0:
        time = int(input("Enter the time in years: "))
        if time <= 0:
            print("\n\tThe time can't be less than or equal to 0 years!")


    print(f"\nPrincipal Amount = ${Principle}")
    print(f"Interest Rate = {rate}%")
    print(f"Time = {time}years")

    Compound_Interest = Principle * pow(1 + rate / 100 , time)

    print(f"\nFinal Amount = {Principle} x (1 + {rate} / 100)^{time} ")

    print(f"\n\t\t\tAns = ${Compound_Interest :.4f}")

    '''while True:
        Principle = float(input("\nEnter the initial Principle Amount balance: "))
        if Principle < 0:
            print("Can't be less than 0")
        else:
            break'''
except ValueError as err:
    print(f"ERROR : {err}")

finally:
    print("\n                            THANK YOU , BYE!                           ")
    print("-----------------------------------------------------------------------")
6