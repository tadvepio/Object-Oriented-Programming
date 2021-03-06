"""
Created 6.02.2021
@File: mammal.py
@Description: The mammal class
@author: Tapio Koskinen

"""

class Mammal:

    def __init__(self, ID, spe, n, s, w, h, noise, diet):
        self.ID = ID
        self.species = spe
        self.name = n
        self.size = s
        self.weight = w
        self.height = h
        self.noise = noise
        self.diet = diet
    
    def noise(self):
    	return self.noise

    def __str__(self):
    	return f"Species: {self.species}\
    	\nName: {self.name}\
    	\nSize: {self.size}\
    	\nWeight: {self.weight} kg\
    	\nHeight: {self.height} m\
    	\nNoise: {self.noise}\
    	\nDiet: {self.diet}"
