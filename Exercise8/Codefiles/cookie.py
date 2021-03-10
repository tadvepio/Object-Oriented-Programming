# OOP exercise 8, Task 3
# Author: Tapio Koskinen
# 8.3.2021

import random

class Cookie:

    def __init__(self, shape, flavor="No flavor"):
        self.__shape = shape
        self.__flavor = flavor
        self.__frosted = "No"
        self.__baked = "No"

    flavors = ["Chocolate", "Vanilla", "Toffee", "White chocolate", "Banana"]
    
    def set_shape(self):
        self.__shape = input("Set cookie shape: ")

    def get_shape(self):
        return self.__shape

    def set_flavor(self):
        self.__flavor = input("Set flavor: ")
    
    def set_random_flavor(self):
        self.__flavor = self.flavors[random.randint(0,len(self.flavors)-1)]

    def get_flavor(self):
        return self.__flavor

    def set_frosted(self):
        if self.__frosted == "No":
            self.__frosted = "Yes"
        else:
            return self.__frosted

    def get_frosted(self):
        return self.__frosted
    
    def set_baked(self):
        if self.__baked == "No":
            self.__baked = "Yes"
        else:
            return self.__baked

    def get_baked(self):
        return self.__baked

    def __str__(self):
        return f"Your cookie:\nShape: {self.get_shape()}\nFlavor: {self.get_flavor()}\nBaked: {self.get_baked()}\nFrosted: {self.get_frosted()} "