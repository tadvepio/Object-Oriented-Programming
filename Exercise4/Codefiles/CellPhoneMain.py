"""
Created 6.02.2021
@File: CellPhoneMain.py
@Description: The Main for CellPhone
@author: Tapio Koskinen

"""

import CellPhone_demo

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

main()



