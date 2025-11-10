import string
import time

password = input("Enter Password: ")
start = time.time()
chars = string.ascii_lowercase
guess = []
for val in range(5):
    a = [i for i in chars]
    #print(a)
    for y in range(val):
        a = [x+i for i in chars for x in a]
    guess = guess+a
    #print(guess)
    if password in guess:
        break

end = time.time()

clock = str(end - start)

print("Your password: " + password)
print("Time taken: " + clock)
