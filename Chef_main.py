from Chef import Chef
from ChineseChef import ChineseChef

print("----------------------------------------------------------")
print("                       CHEF                               ")
print("----------------------------------------------------------")

chef1 = Chef("Oscar Kariuki",20)
print("\nChef's Name: " + chef1.name)
print("Chef's Age: " + str(chef1.age))
chef1.MakeChicken()
chef1.MakeSalad()
chef1.MakeSpecialDish()

print("\n----------------------------------------------------------")
print("                       CHINESE_CHEF                       ")
print("----------------------------------------------------------")


chef2 = ChineseChef("Samohong",25)
print("\nChef's Name: " + chef2.name)
print("Chef's Age: " + str(chef2.age))
chef2.MakeChicken()
chef2.MakeSalad()
chef2.MakeFriedRice()
chef2.MakeSpecialDish()

print("----------------------------------------------------------")
