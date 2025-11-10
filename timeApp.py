import time

print("------------------------------------------------------------------------")
print("                           COUNTDOWN TIME APP                           ")
print("------------------------------------------------------------------------")

try:

    myTime = int(input("\nEnter the time in seconds: "))

    print(f"\nTime = {myTime}s")

    #for x in reversed(range(0,myTime)): - prints from backwards
    for x in range(myTime,0,-1):#same to the reversed range
        #print(x)
        seconds = x % 60
        minutes = int(x / 60 ) % 60
        hours = int(x / 3600) % 24
        print(f"\t\t\t{hours:02}:{minutes:02}:{seconds:02}")
        time.sleep(1)

    print("\n\t\t\t\t\t\t~ TIME'S UP!")

except ValueError as err:
    print(f"\tERROR : {err}")

print("------------------------------------------------------------------------")

#print(int(3605 / 3600) % 24 )

