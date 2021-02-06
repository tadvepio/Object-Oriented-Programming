"""
Created 6.02.2021
@File: car_demo.py
@Description: Car class
@author: Tapio Koskinen

"""

class Car:

    def __init__(self):
        self.__maker = None
        self.__model = None
        self.__mileage = None
        self.__price = None
        self.__color = None
        self.__maximum_load = None
        self.__trunk_size = None
    
    # The getters/Accessors
    def get_maker(self):
        return self.__maker

    def get_model(self):
        return self.__model

    def get_mileage(self):
        return self.__mileage

    def get_price(self):
        return self.__price

    def get_color(self):
        return self.__color

    def get_maximum_load(self):
        return self.__maximum_load

    def get_trunk_size(self):
        return self.__trunk_size

    # The setters/mutators
    def set_maker(self):
        self.__maker = input("Set maker: ")

    def set_model(self):
        self.__model = input("Set model: ")

    def set_mileage(self):
        self.__mileage = int(input("Set mileage: "))

    def set_price(self):
        self.__price = int(input("Set price: "))

    def set_color(self):
        self.__color = input("Set color: ")

    def set_maximum_load(self):
        self.__maximum_load = int(input("Set maximum load limit: "))

    def set_trunk_size(self):
        self.__trunk_size = input("Set trunk size: ")

    def __str__(self):
        return f"""Your car details:\nMaker: {self.get_maker()}\nModel: {self.get_model()}\nMileage: {self.get_mileage()}
Price: {self.get_price()}\nColor: {self.get_color()}\nMaximum load limit: {self.get_maximum_load()}
Trunk size: {self.get_trunk_size()}"""
    

