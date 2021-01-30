# Author: Tapio Koskinen
# File: dice_test.py
# Date: 30.1.2021
# Description: Exercise 3 - part 5,6,7

import Coin_Dice_demo

def main():

	"""# Set the class into dice
	dice = Coin_Dice_demo.Dice()

	print("With my dice, we can decide which color shirt you can use")

	#Ask user to choose instead of rolling
	choise = input("Wanna choose your destiny?(y/n): ")
	if choise == "y":
		dice.cheat()
	if choise == "n":
		dice.roll()

	# Print the value of the dice
	print(f"The dice drops as: {dice.get_sideup()}")

	#Print the color
	print(f"Your shirt color of the day is: {dice.get_color()}")
"""
	
	my_dice = Coin_Dice_demo.Dice()
	notmy_dice = Coin_Dice_demo.Dice()

	my_dice.roll()
	notmy_dice.roll()

	print(my_dice.get_sideup() + notmy_dice.get_sideup())
main()