# OOP Exercise work: Expense Tracker
# Author: Tapio Koskinen
# File: windows.py
# Description: window templates

import PySimpleGUI as sg
from account_generator import user_generator
from user import User
import data_manager
import matplotlib.pyplot as plt
from datetime import datetime, timedelta, date
import datetime

global add_exp
add_exp = []
global add_inc
add_inc = []

def loginscreen():
    sg.theme('DarkAmber') #GUI color scheme
        # Sign in Layout
    signin_layout = [
        [sg.Text('Expense tracker. Create an account or login')],
        [sg.Text("Username:"), sg.InputText()],
        [sg.Text("Password:"), sg.InputText(password_char='*')],
        [sg.Button('Confirm')],
        [sg.Button('Create an account instead')],
    ]

    # Sign in Window
    window = sg.Window('Expense Tracker', signin_layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED: # Close window or cancel to exit
            window.close()
            break
        elif event == 'Confirm':
            datamngr = data_manager.Data_manager()
            result = datamngr.confirm_login(values[0],values[1])
            if result == "OK":
                global user_now
                user_now = values[0]
                window.close()
                home_page()
                break
            elif result == "false":
                print("Uname not found")
            else:
                continue

        elif event == 'Create an account instead':
            window.close()
            account_creation()
            break

def account_creation():
    sg.theme('DarkAmber') #GUI color scheme
    # Creation Layout
    # Asks user for details that will be used in the
    # main page
    creation_layout = [
        [sg.Text('Create an account')],
        [sg.Text("Username:"), sg.InputText()],
        [sg.Text("Password:"), sg.InputText()],
        [sg.Text("First name:"), sg.InputText()],
        [sg.Text("Last name:"), sg.InputText()],
        [sg.Text("Balance:"), sg.InputText()],
        [sg.Text("Monthly income:"),sg.InputText("Amount")],
        [sg.Text("Monthly expenses:"),sg.InputText("Amount")],
        [sg.Text("Next payment date:"),sg.InputText("YYYY-MM-DD")],
        [sg.Button('Submit'), sg.Button('Cancel')]
    ]

    # Creation Window
    window = sg.Window('Expense Tracker', creation_layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # Close window or cancel to exit
            window.close()
            break
        elif event == 'Submit':
            mngr = data_manager.Data_manager()
            mngr.create_user(values[0],values[1])
            mngr.account_details(
                values[0],values[2],
                values[3],values[4],
                values[5],values[6],values[7]
                )
            window.close()
            loginscreen()

# The main page of the program

def home_page():
    sg.theme('DarkAmber') #GUI color scheme
    mngr = data_manager.Data_manager()
    details = mngr.get_details(user_now)
    d1=details[5]
    year, month, day = map(int, d1.split('-'))
    d1 = datetime.date(year, month, day)
    now = datetime.datetime.now()
    d0 = datetime.date(now.year, now.month, now.day)
    delta = d1-d0
    days = delta.days
    moneyperday = int(details[2])//days  
    # Main layout
    main_layout = [
        [sg.Text("Balance: "+details[2]+"\u20ac",font=("Helvetica",20)),\
                    sg.Text("Monthly income: "+details[3]+"\u20ac",font=("Helvetica",20),text_color='green'),\
                        sg.Text("Monthly expenses: "+details[4]+"\u20ac",font=("Helvetica",20),text_color='red')],\
                            [sg.Text("Next payment: "+details[5],font=("Helvetica",20),text_color='green')],\
                            [sg.Text("Money per day: "+str(moneyperday)+"\u20ac",font=("Helvetica",20),text_color='green')],
                                [sg.Button('Modify'),sg.Button('Quit')]
    ]

    # Home window
    window = sg.Window('Expense Tracker', main_layout,size=(900,600))
    while True:
        event, values = window.read() 
        if event == sg.WIN_CLOSED or event == 'Quit': # Close window or cancel to exit
            break
        elif event == 'Modify':
            window.close()
            modify_page()


# Modify income and/or expenses
def modify_page():

    sg.theme('DarkAmber')
    mod_layout = [
        [sg.Text("Income details")],
        [sg.Listbox(values=[i for i in add_inc],size=(20,5))],
        [sg.Text("Expense details")],
        [sg.Listbox(values=[i for i in add_exp],size=(20,5))],
        [sg.Button("Add income"),sg.Button("Add expenses"),sg.Button("Back")]
    ]

    window = sg.Window('Expense Tracker', mod_layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Back": # Close window or cancel to exit
            window.close()
            home_page()
            break
        elif event == "Add income":
            window.close()
            modify_income()
            break
        elif event == "Add expenses":
            window.close()
            modify_expense()
            break



def modify_income():
    mod_income_layout = [
        [sg.Text("Add income")],
        [sg.InputText("YYYY-MM-DD"),sg.InputText("Amount")],
        [sg.Button("Add"),sg.Button("Cancel")]
    ]

    window = sg.Window('Expense Tracker', mod_income_layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Cancel":
            window.close()
            break
        elif event == "Add":
            add_inc.append(str(values[0])+" - "+str(values[1]))
            window.close()
            modify_page()
            break

def modify_expense():
    mod_expense_layout = [
        [sg.Text("Add expense")],
        [sg.InputText("YYYY-MM-DD"),sg.InputText("Amount")],
        [sg.Button("Add"),sg.Button("Cancel")]
    ]

    window = sg.Window('Expense Tracker', mod_expense_layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Cancel":
            window.close()
            home_page()
            break
        elif event == "Add":
            add_exp.append(str(values[0])+" - "+str(values[1]))
            window.close()
            modify_page()
            break


    