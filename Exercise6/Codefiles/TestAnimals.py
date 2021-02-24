"""
Created 24.02.2021
@File: TestAnimals.py
@Description: Inherit mammals, add noise and diet
@author: Tapio Koskinen

"""

from mammal import Mammal


class Dog(Mammal):
    def __init__(self, ID, spe, n, s, w, h):
        super().__init__(ID, spe, n, s, w, h)
        self.noise = "Woof!"
        self.diet = "Dog food"

    def set_noise(self):
        self.noise = input()
    def set_diet(self):
        self.diet = input()
    def get_noise(self):
        return self.noise
    def get_diet(self):
        return self.diet
    def __str__(self):
        return f"{super().__str__()}"+f"\nNoise: {self.noise}\nEats: {self.diet}"

class Cat(Mammal):
    def __init__(self, ID, spe, n, s, w, h):
        super().__init__(ID, spe, n, s, w, h)
        self.noise = "Meow!"
        self.diet = "Cat food"

    def set_noise(self):
        self.noise = input()
    def set_diet(self):
        self.diet = input()
    def get_noise(self):
        return self.noise
    def get_diet(self):
        return self.diet
    def __str__(self):
        return f"{super().__str__()}"+f"\nNoise: {self.noise}\nEats: {self.diet}"