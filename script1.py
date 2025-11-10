#from script2 import *

#print(__name__) #now if script2 is run directly this becomes script1 name
'''
print(dir()) # attributes or variables
print(__name__) #in __name__ it is string of __main__'''

def favourite_food(food):
    print(f"Your favourite food is {food}")
def main():
    print("This is script1")
    favourite_food("Sushi")
    print("Goodbye!")
if __name__ == '__main__': #this checks if the script is run directly if not it won't run the main body main()
    main()