
import automobile

class Suv(automobile.Automobile):

    def __init__(self, make, model, mileage, price, pass_cap):
        automobile.Automobile.__init__(self, make, model, mileage, price)
        self.__pass_cap = pass_cap

    def get_pass_cap(self):
        return self.__pass_cap
    
    def set_pass_cap(self):
        self.__pass_cap = input("Set passenger capacity: ")