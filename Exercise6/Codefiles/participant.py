"""
Created 24.02.2021
@File: participant.py
@Description: Class for participant and the subclasses student/teacher
@author: Tapio Koskinen

"""

class Participant:

    def __init__(self, fname, lname, course, role):
        self.fname = fname
        self.lname = lname
        self.course = course
        self.role = role
    
    def set_fname(self):
        self.fname = input()
    def set_lname(self):
        self.lname = input()
    def set_course(self):
        self.course = input()
    def set_role(self):
        self.role = input()

    def get_fname(self):
        return self.fname
    def get_lname(self):
        return self.lname
    def get_course(self):
        return self.course
    def get_role(self):
        return self.role

    def __str__(self):
        return f"First name: {self.fname}\nLast name: {self.lname}\
            \nCourse: {self.course}\nRole: {self.role}"

class Student(Participant):
    def __init__(self, fname, lname, course, role, yearsInSchool, ID, pet):
        super().__init__(fname, lname, course, role)
        self.yearsInSchool = yearsInSchool
        self.ID = ID
        self.pet = pet

    def set_yearsInSchool(self):
        self.yearsInSchool = int(input())
    def set_ID(self):
        self.ID = int(input())
    def set_pet(self):
        self.pet = input()
    def get_yearsInSchool(self):
        return self.yearsInSchool
    def get_ID(self):
        return self.ID
    def get_pet(self):
        return self.pet
    def __str__(self):
        return f"{super().__str__()}\nYears in school: {self.yearsInSchool}\
            \nID: {self.ID}\n\n{self.fname}'s Domestic pet: \n{self.pet[0]}\
            \n\n{self.fname}'s wild pet: \n{self.pet[1]}\n"

class Teacher(Participant):
    def __init__(self, fname, lname, course, role, Education, Tools, pet):
        super().__init__(fname, lname, course, role)
        self.Education = Education
        self.Tools = Tools
        self.pet = pet
    
    def set_Education(self):
        self.Education = input()
    def set_Tools(self):
        self.Tools = input()
    def set_pet(self):
        self.pet = input()
    def get_Education(self):
        return self.Education
    def get_Tools(self):
        return self.Tools
    def get_pet(self):
        return self.pet
    def __str__(self):
        return f"{super().__str__()}\nEducation: {self.Education}\
            \nTools: {self.Tools}\n\n{self.fname}'s Domestic pet: \n{self.pet[0]}\
            \n\n{self.fname}'s wild pet: \n{self.pet[1]}\n"