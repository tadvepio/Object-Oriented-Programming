# OOP exercise 8
# Author: Tapio Koskinen
# 8.3.2021

class Flat:
    def __init__(self):
        self.__floors = "Dirty"
        self.__windows = "Dirty"
        self.__surfaces = "Dirty"
        self.__bed = "Unmade"
        self.__toilet_paper = "Running out"
        self.__fridge = "Empty"
    
    def set_floors(self,state):
        self.__floors = state
    def get_floors(self):
        return self.__floors
    def set_windows(self,state):
        self.__windows = state
    def get_windows(self):
        return self.__windows
    def set_surface(self,state):
        self.__surfaces = state
    def get_surface(self):
        return self.__surfaces
    def set_bed(self,state):
        self.__bed = state
    def get_bed(self):
        return self.__bed
    def set_toilet_paper(self,state):
        self.__toilet_paper = state
    def get_toilet_paper(self):
        return self.__toilet_paper
    def set_fridge(self,state):
        self.__fridge = state
    def get_fridge(self):
        return self.__fridge

    def __str__(self):
        return f"Floors: {self.get_floors()}\
            \nWindows: {self.get_windows()}\
            \nSurfaces: {self.get_surface()}\
            \nBed: {self.get_bed()}\
            \nToilet paper: {self.get_toilet_paper()}\
            \nFridge: {self.get_fridge()}"