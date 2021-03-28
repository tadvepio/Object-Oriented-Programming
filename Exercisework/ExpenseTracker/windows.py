# OOP Exercise work: Expense Tracker
# Author: Tapio Koskinen
# File: windows.py
# Description: window templates

import PySimpleGUI as sg
from account_generator import user_generator
from user import User
import data_manager
import matplotlib

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
        [sg.Text("Monthly income:"), sg.InputText()],
        [sg.Text("Monthly expenses:"), sg.InputText()],
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
                values[5],values[6]
                )
            window.close()
            loginscreen()

# The main page of the program

def home_page():
    sg.theme('DarkAmber') #GUI color scheme
    mngr = data_manager.Data_manager()
    details = mngr.get_details(user_now)
    user_object = User(details[0],details[1],details[2],details[3],details[4])
    ex_graph =sg.Graph((400,300), (0,0),(200,200),background_color="white",key="graph")
    time_bar = sg.Graph((400,10), (0,0), (0,0), background_color="white", key="times")
    money_bar = sg.Graph((10,300), (0,0), (0,0), background_color="white", key="times")
    filler = sg.Graph((10,0),(0,0),(0,0))  
    # Main layout
    main_layout = [
        [sg.Text('Your details')],\
        [sg.Text(f"First name: {user_object.get_name()}"),\
            sg.Text("Last name: "+details[1]),\
                sg.Text("Balance: "+details[2]+"\u20ac"),\
                    sg.Text("Monthly income: "+details[3]+"\u20ac"),\
                        sg.Text("Monthly expenses: "+details[4]+"\u20ac")],\
                            [money_bar,ex_graph],[filler,time_bar],\
                                [sg.Button('Add income'), sg.Button('Add expense'),sg.Button('Quit')]
    ]

    # Home window
    window = sg.Window('Expense Tracker', main_layout,size=(900,600), finalize=True)
    ex_graph.draw_rectangle(top_left=(0,user_object.get_balance()/10),bottom_right=(20, 0), fill_color="red")
    while True:
        event, values = window.read() 
        if event == sg.WIN_CLOSED or event == 'Quit': # Close window or cancel to exit
            break
        elif event == 'Add income':
            break