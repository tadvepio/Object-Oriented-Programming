# OOP Exercise work: Expense Tracker
# Author: Tapio Koskinen
# File: account_generator.py
# Description: A module that creates accounts

from user import User

def user_generator(fname, lname, balance, minc, mexp):

    fname = fname
    lastname = lname
    balance = float(balance)
    minc = float(minc)
    mexp = float(mexp)

    return User(fname, lastname, balance, minc, mexp)
