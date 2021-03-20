# OOP Exercise work: Expense Tracker
# Author: Tapio Koskinen
# File: account_generator.py
# Description: A module that creates accounts

from user import User

def user_generator(fname, lname, balance):

    fname = fname
    lastname = lname
    balance = float(balance)
    ID = 1

    return User(fname, lastname, balance, ID)
