import cmath
try:
    print("---------------------------------------------------------------")
    print("                       UNIT CONVERTER APP                      ")
    print("---------------------------------------------------------------")

    num1 = float(input("Enter a number in kilometers: "))

    #1km == 0.6214miles

    conversion_factor = 0.6214

    miles = num1 * conversion_factor

    print(f"\nInput = {num1}km")
    print(f"\t\tMiles = {miles : .4}mi")

    num2 = float(input("\nEnter a number in Celsius: "))

    #Celsius to Fahrenheit = (Celsius * 9/5) + 32

    Fahrenheit = (num2 * 9/5) + 32

    print(f"\nInput = {num2}Celsius")
    print(f"\t\tFahrenheit = {Fahrenheit : .4}Fahrenheit")

except ValueError as err:
  print(f"\tERROR : {err}")

finally:
    print("\n                     THANK YOU , BYE!                         ")
    print("---------------------------------------------------------------")
