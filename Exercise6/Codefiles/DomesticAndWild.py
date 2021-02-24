"""
Created 24.02.2021
@File: DomesticAndWild.py
@Description: Sub class domestic and wild animal
@author: Tapio Koskinen

"""

from mammal import Mammal

class Domestic(Mammal):
    def __init__(self, ID, spe, n, s, w, h, noise, diet, attitude):
        super().__init__(ID, spe, n, s, w, h)
        self.noise = noise
        self.diet = diet
        self.attitude = attitude

    def set_noise(self):
        self.noise = input()
    def set_diet(self):
        self.diet = input()
    def set_attitude(self):
        self.attitude = input()
    def get_noise(self):
        return self.noise
    def get_diet(self):
        return self.diet
    def get_attitude(self):
        return self.attitude
    def __str__(self):
        return f"{super().__str__()}"+f"\nNoise: {self.noise}\nEats: {self.diet}\
            \nAttitude: {self.attitude}"


class Wild(Mammal):
    def __init__(self, ID, spe, n, s, w, h, noise, diet, killCount):
        super().__init__(ID, spe, n, s, w, h)
        self.noise = noise
        self.diet = diet
        self.killCount = killCount

    def set_noise(self):
        self.noise = input()
    def set_diet(self):
        self.diet = input()
    def set_killCount(self):
        self.killCount = int(input())
    def get_noise(self):
        return self.noise
    def get_diet(self):
        return self.diet
    def get_killCount(self):
        return self.killCount
    def __str__(self):
        return f"{super().__str__()}"+f"\nNoise: {self.noise}\nEats: {self.diet}\
            \nKillcount: {self.killCount}"
            