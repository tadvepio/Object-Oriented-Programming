"""
Created 30.1.2021
@File: CellPhone.py
@Description: The Cellphone
@author: Tapio Koskinen

"""

import CellPhone_demo

def main():

	my_phone = CellPhone_demo.CellPhone()

	my_phone.set_manufact()

	my_phone.set_model()

	my_phone.set_retailPrice()

	print("Here is the data that you provided:",my_phone)

	my_phone.set_manufact()

	my_phone.set_model()

	my_phone.set_retailPrice()

	print("Here is the data that you provided:",my_phone)

main()



