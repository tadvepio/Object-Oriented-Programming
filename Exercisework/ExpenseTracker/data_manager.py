# OOP Exercise work: Expense Tracker
# Author: Tapio Koskinen
# File: data_manager.py
# Description: Used for manipulating user_data.txt

class Data_manager():

    def create_user(self,uname,passwrd):
        self.__data = open(uname+'.txt','w')
        self.__data.write(passwrd)
        self.__data.close()

    def confirm_login(self,uname,passwrd):
        self.__data = open(uname+'.txt','r')
        for row in self.__data:
            if row == passwrd:
                return "OK"
            else:
                return None
                
    def account_details(self,uname, fname,lname,balance):
        self.__data = open(uname+'_data.txt','w')
        self.__data.write(fname+"\n"+lname+"\n"+balance)
        self.__data.close()