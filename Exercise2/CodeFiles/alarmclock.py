"""
Author: Tapio Koskinen
Date: 22.1.2021
Task: Code an alarm clock

"""

import tkinter as tk

from time import strftime

class clock():
	
	def real_time(self):
		actual_time = strftime('%H:%M:%S')
		return actual_time

	def alarm_time(self):
		
		hour = input()
		minute = input()
		second = input()
		time = hour+":"+minute+":"+":"+second
		return time


	def alarm_state(self):
		
		state = input("Turn on or off?(on/off)")
		if state == "on":
			return True
		elif state == "off":
			return False
		else:
			return "Alarm state undefined"


def the_GUI():

	alarm_clock = clock()
	root = tk.Tk()
	root.title('Alarm Clock')

	lbl = tkinter.Label(text="alarm_clock.real_time()")
	lbl.pack()

	mainloop()

the_GUI()
