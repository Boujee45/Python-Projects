try:
    print("-----------------------------------------------------------------------------")
    print("                                   ODDS ARRAY                                ")
    print("-----------------------------------------------------------------------------")

    Array = [6,7,5,1,8,4,0,9,12,13]
    odds = ""

    for i in range(len(Array)):
        if i % 2 != 0 and Array[i] % 2 != 0:
            if odds:
                odds += " , "

            odds += str(Array[i])

    print(f"Arrays = {Array}")
    print(f"Odds Array = {odds}")
    print(f"\t\t\tAns = {odds}")

except NameError as err:
    print(f"Error: {err}")
finally:
    print("\n-----------------------------------------------------------------------------")
