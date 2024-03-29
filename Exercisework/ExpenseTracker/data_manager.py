# OOP Exercise work: Expense Tracker
# Author: Tapio Koskinen
# File: data_manager.py
# Description: Used for handling user data

import hashlib
from cryptography.fernet import Fernet
from user import User

class Data_manager():

    # Writes down and saves username and the password(converted to hash)
    # into a txt file.
    def create_user(self,uname,passwrd):
        self.__data = open(uname+'.txt','w')
        self.__data.write(hashlib.sha256(passwrd.encode()).hexdigest())
        self.__data.close()

    # Used for checking if the user exists. If it exists, compare
    # the input password as hash to the stored hash.
    def confirm_login(self,uname,passwrd):
        try:
            self.__data = open(uname+'.txt','r')
            for row in self.__data:
                if row == hashlib.sha256(passwrd.encode()).hexdigest():
                    return "OK"
                else:
                    return None
        except FileNotFoundError:
            return "false"

    # Writes the user details in a binaryfile and save it            
    def account_details(self,uname, fname,lname,balance,minc,mexp,pay):
        key = Fernet.generate_key()
        ukey = open(uname+'_key','wb')
        ukey.write(key)
        ukey.close()
        fernet = Fernet(key)
        self.__data = open(uname+'_data','wb')
        flb = fname+"\n"+lname+"\n"+balance+"\n"+minc+"\n"+mexp+"\n"+pay
        flb = flb.encode()
        self.__data.write(fernet.encrypt(flb))
        self.__data.close()

    # Opens data based on username and returns the details as a list.
    def get_details(self,uname):
        ukey = open(uname+'_key','rb')
        key = ukey.read()
        print(type(key))
        ukey.close()
        fernet = Fernet(key)
        data = open(uname+'_data','rb')
        data1 = data.read()
        data.close()
        data2 = fernet.decrypt(data1)
        data2 = data2.decode("utf-8")
        details = data2.split("\n")
        print(details)
        return details


        