class Cal():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def Subtract(self):
        return self.a - self.b
    def Multiply(self):
        return self.a * self.b
    def Division(self):
        return self.a / self.b

print("-----------------------------------------------------")
print("                     CALCULATOR                      ")
print("-----------------------------------------------------")

try:
    a = float(input("Enter a number: "))
    b = float(input("Enter another number: "))

    print("\n\t0. : Exit")
    print("\t1. : Add")
    print("\t2. : Subtract")
    print("\t3. : Multiply")
    print("\t4. : Division")
    print("\t5. : Reset Calculator")
    obj = Cal(a,b)
    Choice = 1
    while Choice != 0:

        Choice = int(input("\nEnter your Choice: "))

        if Choice == 1:
            print(f"\nSol = {a} + {b} \n\t\tAns = {obj.add()}")
        elif Choice == 2:
            print(f"\nSol = {a} - {b} \n\t\tAns = {obj.Subtract()}")
        elif Choice == 3:
            print(f"\nSol = {a} X {b} \n\t\tAns = {obj.Multiply()}")
        elif Choice == 4:
            print(f"\nSol = {a} / {b} \n\t\tAns = {round(obj.Division(),4)}")
        elif Choice == 0:

            print("\nExiting ...")

        elif Choice == 5:
            print("\n-----------------------------------------------------")
            print("                     CALCULATOR                      ")
            print("-----------------------------------------------------")

            a = float(input("\nEnter a number: "))
            b = float(input("Enter another number: "))

            print("\n\t0. : Exit")
            print("\t1. : Add")
            print("\t2. : Subtract")
            print("\t3. : Multiply")
            print("\t4. : Division")
            print("\t5. : Reset Calculator")
            obj = Cal(a, b)


        else:
            print("\nINVALID INPUT!")
    print()
except ZeroDivisionError as err:
    print (f"\n\tERROR : {err}")
except ValueError as err:
    print(f"\n\tERROR : {err}")
except Exception as err:
    print(f"\tERROR : {err}")
finally:
    print("\n           THANKS FOR USING THE APP!               ")
    print("-----------------------------------------------------")

