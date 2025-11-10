import random
import time

try:

    specialNumber = random.randint(0,100)

    count = 0

    guess = ""
    is_running = True

    start = time.time()

    print("-----------------------------------------------------------------------------")
    print("                           GUESSING NUMBER APP                               ")
    print("-----------------------------------------------------------------------------")


    while guess != specialNumber:
        guess = int(input("\nGuess a number: "))
        count += 1
        if guess < specialNumber:
            print("\t\t\t~Too low, try again:")

        elif guess > specialNumber:
            print("\t\t\t~Too high, try again:")

        else:

            end = time.time()

            time = str(end - start)

            print(f"\nGuess = {guess}")
            print(f"Tries = {count}")
            print(f"Time Taken = {time}s")
            print(f"\n\t\t\t~You guessed it! The number is {guess}")

            print(f"\t\t\t~It took {count} tries")


except ValueError as err:
    print(f"\t~Error : {err}")

finally:
    print("\n-----------------------------------------------------------------------------\n\n")

import time

lowest_num = 1
highest_num = 100

Answer = random.randint(lowest_num,highest_num)
is_running = True
guesses = 0

start = time.time()

print("=====================================================================================")
print("                          Python Number Guessing Game                                ")
print("=====================================================================================\n")

print(f"1. Select a number between {lowest_num} and {highest_num}")

while is_running:
    guess = input("\nEnter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("\t\t~That number is out of range.")
            print("\t\t~Please Select a number between {lowest_num} and {highest_num}")

        elif guess < Answer:
            print("\t\t~Too Low! Try Again!")
        elif guess > Answer:
            print("\t\t~Too High! Try Again!")
        else:
            end = time.time()

            time = str(end - start)
            print(f"\nGuess = {Answer}")
            print(f"Attempts = {guesses}")
            print(f"Time Taken = {time}s")

            print(f"\n\t\t~CORRECT! The answer was {Answer}")
            print(f"\t\t~Number of Guesses : {guesses}")
            is_running = False
    else:
        print("\t\t~Invalid Guess")
        print("\t\t~Please Select a number between {lowest_num} and {highest_num}")


print("=====================================================================================")