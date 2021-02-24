

import automobile

class Car(automobile.Automobile):

    def __init__(self, make, model, mileage, price, doors):
        automobile.Automobile.__init__(self, make, model, mileage, price)
        self.__doors = doors

    def set_doors(self, doors):
        self.__doors = input("Set number of doors: ")

    def get_doors(self):
        return self.__doors