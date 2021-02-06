"""
Created 6.02.2021
@File: car_main.py
@Description: Car main
@author: Tapio Koskinen

"""
# Import car class, mammal, dice and finally random
from car_demo import Car
from mammal import Mammal
from Dice_demo import Dice
import random

# main function

def main():

    # Make an instance of Car() and set all the values
    my_car = Car()

    my_car.set_maker()
    my_car.set_model()
    my_car.set_mileage()
    my_car.set_price()
    my_car.set_color()
    my_car.set_maximum_load()
    my_car.set_trunk_size()

    print(my_car)
    
    # Create a zoo with 6 animal instances of the Mammal class
    zoo = []

    animal1 = Mammal(1,"Monkey","Fred","small",10,0.5)
    animal2 = Mammal(2,"Horse","Lisa","large",700,2.5)
    animal3 = Mammal(3,"Bear","Fred","large",1100,3)
    animal4 = Mammal(4,"Dog","Fifi","small",2,0.3)
    animal5 = Mammal(5,"Cat","Simba","small",1,0.3)
    animal6 = Mammal(6,"Whale","Larry","large",70000,30)

    # same as .append() but allows to append in sequence
    zoo.extend((animal4,animal2,animal1,animal6,animal5,animal3))

    # The Dice requires an owner on initialization
    dice = Dice("Lucky lady")

    dice.roll()

    print("\nNumber from dice:",dice.get_sideup())

    # Iterate through the zoo and find an animal with the same id as the dice.sideup
    for i in zoo:
        if i.ID == dice.get_sideup():
            # If the animal is small and it's weight is less than maximum load, it fits.
            if i.size == "small" and my_car.get_maximum_load() >= i.weight:
                print(f"{i.name} the {i.species} fits in the trunk!")
            # Else it doesn't
            else:
                print(f"{i.name} the {i.species} does not fit in the trunk!")
        else:
            continue

main()
