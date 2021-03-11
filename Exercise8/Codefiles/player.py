# Exercise 8 task 5
# Player class
# Author: Tapio Koskinen

class Player:

    def __init__(self, name):
        self.__name = name
        self.__score = 0
        self.__practice_score = 0

    def set_name(self):
        self.__name = input("Set player name: ")
    
    def get_name(self):
        return self.__name

    def set_score(self, score):
        self.__score = score

    def get_score(self):
        return self.__score

    def set_practice_score(self, score):
        self.__practice_score = score

    def get_practice_score(self):
        return self.__practice_score
    
    def __str__(self):
        return f"Name: {self.get_name()}\
            \nScore: {self.get_score()}/10\
            \nPractice score: {self.get_practice_score()}/10"