

class Automobile:

    def __init__(self, make, model, mileage, price):
        self.__make = make
        self.__model = model
        self.__mileage = mileage
        self.__price = price
    
    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_mileage(self):
        return self.__mileage
    
    def get_price(self):
        return self.__price

    def set_maker(self):
        self.__make = input("Set maker: ")

    def set_model(self):
        self.__model = input("Set model: ")

    def set_mileage(self):
        self.__mileage = input("Set mileage: ")

    def set_price(self):
        self.__price = input("Set price: ")

    def __str__(self):
        print("Hello")