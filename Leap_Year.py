print("-----------------------------------------------------")
print("                 LEAP_YEAR CHECKER APP               ")
print("-----------------------------------------------------")

try:

    year = int(input("\nEnter a year: "))

    if year % 400 == 0 and year % 100 == 0:
        print(f"\n\t~ {year} is a leap year.")
    elif year % 4 == 0 and year % 100 != 0:
        print(f"\n\t~ {year} is a leap year.")
    else:
        print(f"\n\t~ {year} is not a leap year.")

except ValueError as err:
    print(err)

finally:
    print("\n                  THANK YOU , BYE!                   ")
    print("-----------------------------------------------------")
