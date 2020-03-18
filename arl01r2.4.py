"""R. IÑIGO S. ARCANGEL
   DATALOG Lab01
   Feb. 9, 2020
   I have neither received nor provided any help on this (lab) activity, nor
   have I concealed any violation of the Honor Code."""


class Flower:
    def __init__(self, petalName, petalNumber, petalPrice): #Constructor or Initializer
        self.name = petalName #Representing the instances of the class
        self.petals = petalNumber
        self.price = petalPrice

    def getName(self): # Represents the name of the flower
        return self.name

    def getPetals(self): # Represents the number of petals of the flower
        return self.petals

    def getPrice(self): # Represents the price of the flower
        return self.price

f1 = Flower("Rose", 6, 1000)
print("FLOWER DETAILS: ")
print("Name of the flower: ")
print(f1.getName()) # to print the name of the flower that was inputted
print("Number of petals: ")
print(f1.getPetals()) # to print the number of petals of the flower that was inputted
print("Price of the flower: ")
print(f1.getPrice()) # to print the inputted price of the flower

