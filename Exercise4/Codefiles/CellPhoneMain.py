"""
Created 6.02.2021
@File: CellPhoneMain.py
@Description: The Main for CellPhone
@author: Tapio Koskinen

"""

import CellPhone_demo
from Dice_demo import Dice
import random

def main():

	my_phone = CellPhone_demo.CellPhone(1)
	your_phone = CellPhone_demo.CellPhone(2)

	print("Data for my phone:",my_phone,"\nData for your phone:",your_phone)

	my_phone.set_manufact()

	my_phone.set_model()

	my_phone.set_retailPrice()

	your_phone.set_manufact()

	your_phone.set_model()

	your_phone.set_retailPrice()

	print("Data for my phone:",my_phone,"\nData for your phone:",your_phone)

	print("\nLet us roll some dice\n")

	dice = Dice("referee")
	
	rolling = True

	while rolling:
		dice.roll()
		num = int(dice.get_sideup())
		if num == int(my_phone.get_ID()):
			print(f"""The phone with id: {my_phone.get_ID()} wins!""")
			break
		elif num == int(your_phone.get_ID()):
			print(f"""The phone with id: {your_phone.get_ID()} wins!""")
			break
		else:
			continue		

main()
