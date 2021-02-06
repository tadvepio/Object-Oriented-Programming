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