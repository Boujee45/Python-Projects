#Python 2d Lists and Tuples

fruits = ["apple","bananas","oranges"]
vegetables = ["celery","carrots","kales"]
meat = ["chicken","fish","beef"]

groceries = [fruits,vegetables,meat]

for collection in groceries:
    for food in collection:
        #print(food)
        print(food,end=" ")
        '''print(groceries)
        print(groceries[0])
        print(groceries[1])
        print(groceries[2])

        print(groceries[0][0])
        print(groceries[1][1])
        print(groceries[2][2])'''
    print()

num_pad = ((1,2,3),(4,5,6),(7,8,9),("*",0,"#"))

for x in num_pad:
    for y in x:
        print(y,end=" ")

    print()

#Python Dictionary

Calendar = {"Jan":"January",
            "Feb":"February",
            "Mar":"March",
            "Apr":"April",
            "May":"May",
            "Jun":"June",
            "Jul":"July"}

if Calendar.get("Jun"):
   print(Calendar.get("Jun"))
else:
    print("Invalid Month")

#print(dir(Calendar))
#print(help(Calendar))

Calendar.update({"Aug":"August"})

Calendar.pop("Aug")

#Calendar.popitem()

#Calendar.clear()

print(Calendar)

#Keys = Calendar.keys()
#print(Keys)

#Values = Calendar.values()
#print(Values)

#Items = Calendar.items()
#print(Items)

for keys in Calendar.keys():
    print(keys)

for values in Calendar.values():
    print(values)

for items in Calendar.items():
    print(items)

for key,value in Calendar.items():
    print(f"{key}:{value}")

#---Lists comprehension---

'''doubles = []

for x in range(1,11):
    doubles.append(x * 2)
    
print(doubles)'''

#-----------------------------------------------------------------------
#list comprehension = [expression for value in iterable if condition]

double = [x * 2 for x in range(1,11)]
squares = [y * y for y in range(1,11)]
triples = [z * 3 for z in range(1,11)]

fruits = ["apples","bananas","oranges","tomatoes"]

fruits = [fruit.upper() for fruit in fruits]
fruit_chars = [fruit[0] for fruit in fruits]

numbers = [1,-2,3,-4,5,-6,7,8,9]
positive_nums = [num for num in numbers if num >= 0]
negative_nums = [num for num in numbers if num <= 0]

grades = [30,40,50,55,60,70,80,90,95,75,45]
passing_grades = [grade for grade in grades if grade >= 60]

print()

print(double)
print(squares)
print(triples)

print()

print(fruits)
print(fruit_chars)

print()

print(positive_nums)
print(negative_nums)

print()

print(passing_grades)