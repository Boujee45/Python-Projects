import time

#positional argument

def happy_birthday(name,age):
    print(f"\nHappy birthday to {name}")
    print(f"You are now {age} years old.")
    print("Happy Birthday!\n")

happy_birthday("John",20)
happy_birthday("Jane",30)


#default arguments

def count(end,start=0):
    for x in range(start,end+1):
        print(x, end=" ")
        time.sleep(0.2)
    print("DONE!")
    print()

count(10)


#keyword arguments

#print(line, end="")-end="" is a keyword argument
#print(line, sep="-")-sep="-" is a keyword argument

def get_phone(country,area,first,last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(area=123,country=1,first=456,last=789)

print(phone_num)
print()

#Arbitrary arguments

def add(*args):
    total=0
    for arg in args:
        total += arg
    return  total

#you can change *args to any name but the unpacking operator(*) remains e.g *nums

print(add(45,90,50))
print()

def print_address(**kwargs):
    #pass
    #values
    #for value in kwargs.values():
        #print(value, end=" ")

    #keys
    #for key in kwargs.keys():
        #print(key, end=" ")

    #items key value pairs
    for key,value in kwargs.items():
        print(f"{key}: {value}")
    print()
print_address(street="123 Fake St.",
              city="Detroit",
              state="MI",
              zip="1204")

def shipping_label(*args,**kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "PoBox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('PoBox')}")
    else:
        print(f"{kwargs.get('street')}")

    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")

shipping_label("Dr.","Spongebob","Square_pants"
               ,street="123 fake St.",
               city="Detroit",
               apt="#100",
               PoBox = "#1001",
               state="MI",
               zip="54321")
