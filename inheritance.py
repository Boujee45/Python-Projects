class Animal:
    def __init__(self,name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting.")

class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing.")

class Rabbit(Prey):
    def diet(self):
        print(f"{self.name} eats carrots.")

class Hawk(Predator):
    pass
class Fish(Prey, Predator):
    pass

rabbit = Rabbit("Peter")
hawk = Hawk("Tony")
fish = Fish("Nemo")

fish.hunt()
rabbit.diet()
fish.flee()

rabbit.flee()
hawk.hunt()

fish.sleep()
rabbit.eat()