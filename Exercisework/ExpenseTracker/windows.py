# OOP Exercise work: Expense Tracker
# Author: Tapio Koskinen
# File: windows.py
# Description: window templates

import PySimpleGUI as sg
from account_generator import user_generator
from user import User
import data_manager

def loginscreen():
    sg.theme('DarkAmber') #GUI color scheme
        # Sign in Layout
    signin_layout = [
        [sg.Text('Expense tracker. Create an account or login')],
        [sg.Text("Username:"), sg.InputText()],
        [sg.Text("Password:"), sg.InputText()],
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
            else:
                break

        elif event == 'Create an account instead':
            window.close()
            account_creation()
            break

def account_creation():
    sg.theme('DarkAmber') #GUI color scheme
    # Creation Layout
    creation_layout = [
        [sg.Text('Create an account')],
        [sg.Text("Username:"), sg.InputText()],
        [sg.Text("Password:"), sg.InputText()],
        [sg.Text("First name:"), sg.InputText()],
        [sg.Text("Last name:"), sg.InputText()],
        [sg.Text("Balance:"), sg.InputText()],
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
            mngr.account_details(values[0],values[2],values[3],values[4])
            window.close()
            loginscreen()

def home_page():
    a = open(user_now+"_data.txt","r")
    d = []
    for line in a:
        d.append(line)
    print(d)
    sg.theme('DarkAmber') #GUI color scheme
        # Main layout
    main_layout = [
        [sg.Text('Your details')],
        [sg.Text("First name:")],
        [sg.Text("Last name:")],
        [sg.Text("Balance:","\u20ac")],
    ]

    # Home window
    window = sg.Window('Expense Tracker', main_layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # Close window or cancel to exit
            break