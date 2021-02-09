"""
Created 8.2.2021
@File: student_class.py
@Description: A class for a student object
@author: Tapio Koskinen

"""

class Student:

    def __init__(self, fn, ln, sid):
        self.__name = fn
        self.__lastname = ln
        self.__SID = sid
    
    def get_name(self):
        return self.__name
    
    def get_lastname(self):
        return self.__lastname
    
    def get_sid(self):
        return self.__SID

    def set_name(self):
        newname = input("Set first name: ")
        self.__name = newname

    def set_lastname(self):
        newname = input("Set last name")
        self.__lastname = newname

    def set_sid(self):
        newsid = int(input("Set new ID: "))
        self.__SID = newsid

    def __str__(self):
        return f"Name: {self.get_name()}\nLast name: {self.get_lastname()} \nStudent ID: {self.get_sid()}"

