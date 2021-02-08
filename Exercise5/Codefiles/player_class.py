"""
Created 8.2.2021
@File: player_class.py
@Description: A class for a player object
@author: Tapio Koskinen

"""

class Player:

    def __init__(self, fn, ln, id):
        self.__name = fn
        self.__lastname = ln
        self.__ID = id
    
    def get_name(self):
        return self.__name
    
    def get_lastname(self):
        return self.__lastname
    
    def get_id(self):
        return self.__ID

    def set_name(self):
        newname = input("Set first name: ")
        self.__name = newname

    def set_lastname(self):
        newname = input("Set last name")
        self.__lastname = newname

    def set_id(self):
        newid = int(input("Set new ID: "))
        self.__ID = newid

    def __str__(self):
        print(f"Name: {self.get_name()}\nLastname: {self.get_lastname()} \n ID:{self.get_id()}")

