from script1 import *
#print(__name__) #it is the name of the script name now if script is run directly
def favourite_drink(drink):
    print(f"Your favourite drink is {drink}")

def main():
    print("This is script 2")
    favourite_drink("soda")
    favourite_food("pizza") #you can import the function but not the main body of script 1
    print("Goodbye!")

if __name__ == "__main__": #now this makes it a standalone program
    main()