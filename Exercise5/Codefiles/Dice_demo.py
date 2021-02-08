"""
Created 30.1.2021
@File: Dice_demo.py
@Description: The dice
@author: Tapio Koskinen

"""

import random

# New class Dice

class Dice:

	# Define the data on initalization
	def __init__(self, owner,):
		self.__owner = owner
		self.sideup = "None"
		self.color = "None"
		self.color_list = {1:"Red",2:"Green",3:"Blue",4:"Yellow",5:"Orange",6:"Purple"}

	#Get the owner
	def get_owner(self):
		return self.__owner

	# Similar to coin, get the side up
	def get_sideup(self):
		return self.sideup

	# Get the color facing up
	def get_color(self):
		return self.color

	# Similar to coin, but rolling a number and a color
	def roll(self):
		self.sideup = random.randint(1,6)
		self.color = self.color_list[self.sideup]

	# cheat the outcome
	def cheat(self):
		cheat_value = int(input("1-6: "))
		if cheat_value > 6:
			self.sideup = cheat_value%6
			self.color = self.color_list[self.sideup]
		else:
			self.sideup = cheat_value
			self.color = self.color_list[self.sideup]
	
	def __str__(self):
		return f"Dice owner: {self.get_owner()}"


