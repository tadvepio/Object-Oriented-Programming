"""
Created 6.02.2021
@File: mammal.py
@Description: The mammal class
@author: Tapio Koskinen

"""

class Mammal:

    def __init__(self, ID, spe, n, s, w, h):
        self.ID = ID
        self.species = spe
        self.name = n
        self.size = s
        self.weight = w
        self.height = h
    
    def __str__(self):
        return f"ID: {self.ID}\nSpecies: {self.species}\nSize: {self.size}\nWeight: {self.weight} kg\nHeight: {self.height} m"