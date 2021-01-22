"""
Created on mon jan 18 12:40 2021
@File:
@Description: The Coin simulates a coin that can be flipped
@author: tkoskinen

"""

import random

class Coin:

	# The __init__ method initializes the sideup data attribute with heads

	def __init__(self):
		self.sideup = 'Heads'

	# The toss method generate a random number
	# in the range of 0 through 1. If the number is
	# 0, then sideup is set to 'Heads', otherwise sideup
	# is set to 'Tails'.

	def toss(self):
		

		index = random.randint(0,3)

		#Not so realistically, all have equal chances of happening.

		if index == 0:
			self.sideup = 'Heads'
		elif index == 1:
			self.sideup = 'Tails'
			#Coin lands upright
		elif index == 2:
			self.sideup = 'Upright'
			#Coin flies off
		elif index == 3:
			self.sideup = 'None'

	# The get_sideup method returns the value referenced by sideup

	def get_sideup(self):
		return self.sideup


# The main function

def main():

	# Create an object from the Coin class.
	my_coin = Coin()

	# Display the side of the coin that is facing up.
	print('This side is up:', my_coin.get_sideup())

	#Toss the coin.
	print('I am tossing the coin...')
	my_coin.toss()

	# Display the side of the coin that is facing up.
	if my_coin.get_sideup() == 'Heads' or my_coin.get_sideup() == 'Tails':
		print('This side is up:', my_coin.get_sideup())
	
	#if the value is Upright print another message
	elif my_coin.get_sideup() == 'Upright':
		print('The coin landed', my_coin.get_sideup())
	
	#if the value is None, print the following text
	elif my_coin.get_sideup() == 'None':
		print("The coin dropped into a rabbit hole")

# Call the main function
main()