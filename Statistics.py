print("----------------------------------------------------------------------")
print("                               STATISTICS                             ")
print("----------------------------------------------------------------------")


num = [1,5,4.25]
Sum = 0
Min = 0
Max = 0
Average = 0
Calc = ""

for index, i in enumerate(num):
    Sum += i

    if Calc:
        Calc += " + "
    Calc += str(i)


Min = min(num)
Max = max(num)
Average = Sum / len(num)

print(f"\nArray = {num}")
print(f"\nCalc Sum = {Calc}")
print(f"Sum = {Sum}")
print(f"\nMin = {Min}")
print(f"Max = {Max}")
print(f"\nCalc Average = {Sum} / {len(num)}")
print(f"Average = {Average:.2F}")

print("\n----------------------------------------------------------------------")





