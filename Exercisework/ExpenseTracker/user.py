# OOP Exercise work: Expense Tracker
#
# Author: Tapio Koskinen
# File: user.py
# Description: user class

class User:
    def __init__(self, name, lastname, balance, minc, mexp):
        self.__name = name
        self.__lastname = lastname
        self.__balance = int(balance)
        self.__monthly_income = minc
        self.__monthly_expenses = mexp

    def set_name(self,name):
        self.__name = name
    def get_name(self):
        return self.__name
    
    def set_lastname(self,lastname):
        self.__lastname = lastname
    def get_lastname(self):
        return self.__lastname
    
    def set_balance(self, balance):
        self.__balance = balance
    def get_balance(self):
        return self.__balance
    def add_to_balance(self,add):
        self.__balance += add
    def subtract_from_balance(self, sub):
        self.__balance -= sub
    
    def set_monthly_income(self, inc):
        self.__monthly_income = inc
    def get_monthly_income(self):
        return self.__monthly_income
    
    def set_monthly_expenses(self,exp):
        self.__monthly_expense = exp
    def get_monthly_expenses(self):
        return self.__monthly_expenses

    def __str__(self):
        return f"Firstname: {self.get_name()}\nLastname: {self.get_lastname()}\
            \nBalance: {self.get_balance()}"