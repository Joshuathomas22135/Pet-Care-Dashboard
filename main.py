"""Write a python program to build a Pet Care Dashboard using Python object-oriented programming. They will create a parent Pet class and different
child pet classes, override methods, protect private health data using encapsulation, and update pet health safely with setter methods. The program also
uses a loop to show polymorphism in action across different pet objects. """

class Pet:
    def __init__(self, name, health):
        self.name = name
        self.__health = health

    def info(self):
        print(f"Pet Name: {self.name}\nPet Health Level: {self.__health}")

    def careAction(self):
        print(f"{self.name} needs general care")

    def setHealth(self, newHealth):
        if newHealth >= 1 and newHealth < 100:
            self.__health = newHealth
            print(f"{self.name}'s health has updated to {self.__health}")
        else:
            print("Health must be between 1 to 100")

class Dog(Pet):
    def careAction(self):
        print(f"{self.name} needs a walk and some playtime.")

class Cat(Pet):
    def careAction(self):
        print(f"{self.name} needs grooming and quiet rest.")

class Rabbit(Pet):
    def careAction(self):
        print(f"{self.name} needs fresh carrots and a clean cage.")


dog = Dog("Rocky", 85)
cat = Cat("Luna", 75)
rabbit = Rabbit("Coco", 65)

pets = [dog, cat, rabbit]

print("Pet Care Dashboard")
for pet in pets:
    pet.info()
    pet.careAction()
    print()

print("\n")
print("Updated Pet Health")

dog.setHealth(90)
cat.setHealth(80)
rabbit.setHealth(70)

print()
print("Summary")
for pet in pets:
    pet.info()
    print()