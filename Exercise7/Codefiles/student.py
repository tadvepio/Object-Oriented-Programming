# Task 5. Implement UML diagram
# Author: Tapio Koskinen

class Student:
    def __init__(self,first_name,last_name,student_ID):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__student_ID = student_ID
        self.__pets = []

    def set_first_name(self):
        self.__first_name = input("Enter first name: ")
    def get_first_name(self):
        return self.__first_name
    def set_last_name(self):
        self.__last_name = input("Enter last name: ")
    def get_last_name(self):
        return self.__last_name
    def set_student_ID(self):
        self.__student_ID = int(input("Set user ID: "))
    def get_studnet_ID(self):
        return self.__student_ID
    def add_pets(self,pet):
        self.__pets.append(pet)
    def remove_pets(self,pet):
        self.__pets.pop(pet)
    def print_pets(self):
        for i in range(len(self.__pets)):
            return f"{self.__pets[i]}"
    def __str__(self):
        return f"First name: {self.get_first_name()}\
            \nLast name: {self.get_last_name()}\
            \nStudent ID: {self.get_studnet_ID()}\
            \nPets: \n{self.print_pets()}"