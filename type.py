import math
import cmath



age = 33

#age = float(age) - typecasting to float
#age = str(age) - typecasting to string

name = "Oscar"
#name = bool(name) - typecasting to bool


area = 55

print(f"Area: {area}cm^2")
#power 2 - Numlock + Alt + 0178

temp = 30

print(f"Temp: {temp}")
#degree symbol = Numlock + Alt + 0176

num = 33
result = "Positive" if num > 0 else "Negative"
#ternary operator(X if condition else Y

print(result)



print(type(age))

print(help(str))

print(help(math))

print(help(cmath))

Credit_Number = "1234-5678-9233-4566"
#String methods

print(Credit_Number[0])
print(Credit_Number[:4])
print(Credit_Number[5:])
print(Credit_Number[5:9])
print(Credit_Number[-3])
print(Credit_Number[::2])
print(Credit_Number[2:])
print(Credit_Number[::-1])#reverse

Last_Digits = Credit_Number[-4:]

print(f"xxxx-xxxx-xxxx-{Last_Digits}")

Price1 = 30000.145588

#format specifiers
print(f"Price is: {Price1:.3f}")#decimal places
print(f"Price is: {Price1: 20}")#spacing
print(f"Price is: {Price1:+}")#Addition sign to a positive no.
print(f"Price is: {Price1: }")#negative sign to a negative no.

print(f"Price is: {Price1:,}")#Comma to separate 1000th place value
print(f"Price is: {Price1:< 10}")#left justify
print(f"Price is: {Price1:> 10}")#right justify
print(f"Price is: {Price1:^ 10}")#center align
print(f"Price is: {Price1:+,.3f}")#combination

