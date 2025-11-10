
'''for x in range(3):#prints 3 times(nested loop)
    for y in range(1,10):
        #print(x , end = "\n")#prints in different lines
        #print(x , end = "") #- same line
        #print(x)
         print(y , end= "")
         print()#Gives a new line'''

try:
    print("-------------------------------------------------------------------")
    print("                            GEOMETRY                               ")
    print("-------------------------------------------------------------------")

    rows = int(input("\nEnter the number of rows: "))
    columns = int(input("Enter the number of columns: "))
    symbol = input("Enter a symbol to use: ")

    print(f"\nRows = {rows}")
    print(f"Columns = {columns}")
    print(f"Symbol = {symbol}")

    print()
    for  x in range(rows):
        for y in range(columns):
            print(symbol,end="")

        print()


except ValueError as err:
    print(f"\tERROR : {err}")

print("-------------------------------------------------------------------")


