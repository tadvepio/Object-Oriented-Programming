"""
Created 24.02.2021
@File: main.py
@Description: test file for classes and subclasses
@author: Tapio Koskinen

"""

from DomesticAndWild import Domestic, Wild
from mammal import Mammal
from participant import *

def main():

    Fred = Domestic(1, "Dog", "Fred", "Small", 7, 1, "Woof", "Dog food", "Friendly")

    Molly = Domestic(2, "Cat", "Molly", "Small", 2, 0.4, "Meow", "Cat food", "Suspicious")

    Smooch = Domestic(3, "Hamster", "Smooch", "Small", 0.2, 0.1, "Tsktsk", "Seeds", "Clever")

    Scar = Wild(4, "Lion", "Scar", "Large", 2, 160, "ROAR", "Buffalos", 57)

    Baloo = Wild(5, "Bear", "Baloo", "Large", 2, 220, "OARGH", "Berries and small critters", 20)

    Kong = Wild(6, "Gorilla", "Kong", "Large", 2, 150, "WHOO-OOH", "Fruits", 4)

    Domestics = [Fred, Molly, Smooch]
    Wilds = [Scar, Baloo, Kong]
    """  
    print("\nDomestic animals:\n")
    for i in Domestics:
        print(i)
        print("")
    print("Wild animals:\n")    
    for i in Wilds:
        print(i)
        print("")

"""
    Jimmy = Student(
        "Jimmy", 
        "Buffet", 
        "OOP", 
        "Student",
        3, 
        123456,
        [Domestics[0],Wilds[0]])
    Sally = Student(
        "Sally", 
        "Singer", 
        "OOP", 
        "Student", 
        2, 
        654321,
        [Domestics[1],Wilds[1]])

    Hector = Teacher("Hector", "Cruise", "OOP", "Teacher", "IT-masters",\
        "laptop, useful software",[Domestics[2],Wilds[2]])
    print("*"*30)
    print(f"\nSudents:\n \n{Jimmy}\n")
    print("*"*30)
    print(f"\n{Sally}\n")
    print("*"*30)
    print(f"\nTeacher:\n \n{Hector}")


main()
