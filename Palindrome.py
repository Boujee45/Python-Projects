#Palindrome - returns true when a string written in reversed is the same as the original string

print("===============================================================")
print("                          PALINDROME                           ")
print("===============================================================")

is_Alive = True

while is_Alive:
    Quiz = input("\nEnter a palindrome(q to quit): ").lower()

    Palindrome = Quiz[::-1]

    if Quiz == "q":
        break
    elif Quiz == Palindrome:
        print("\n~TRUE")
        print(f"~{Quiz} is a palindrome.")
    else:
        print("\n~FALSE")
        print(f"~{Quiz} is not a palindrome!,Try Again!")


my_str = input("\nEnter a palindrome: ")

my_str = my_str.casefold()

rev_str = reversed(my_str)


if list(my_str) == list(rev_str):
    print("Yes!, it is a palindrome.")
else:
    print("No!, it is not a palindrome")
 
print("\n===============================================================")
