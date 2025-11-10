print("-----------------------------------------------------------------------")
print("                            ARRAY PRODUCT                              ")
print("-----------------------------------------------------------------------")


Array = {2,3,4}
product = 1
Multiply = ""
lastIndex = len(Array) - 1

for index, i in enumerate(Array):
    product *= i
    if index == lastIndex:
        Multiply += str(i)
    else:
        Multiply += str(i) + " x "

    '''if Multiply:
        Multiply += " x "
    Multiply += str(i)'''

print(f"Array = {Array}")
print(f"Product = {Multiply}")
print(f"Array Product = {product}")


print("\n-----------------------------------------------------------------------")
