# Task 5. Implement UML diagram
# Author: Tapio Koskinen

class Pet:
    def __init__(self, species, name, owner):
        self.__species = species
        self.__name = name
        self.__owner = owner
        
    def set_species(self):
        self.__species = input("Assign species: ")
    def get_species(self):
        return self.__species
    def set_name(self):
        self.__name = input("Set pet name: ")
    def get_name(self):
        return self.__name
    def set_owner(self):
        self.__owner = input("Who owns this pet: ")
    def get_owner(self):
        return self.__owner


    def __str__(self):
        return f"Pet species: {self.get_species()}\
            \nPet name: {self.get_name()}"
