"""
Created 30.1.2021
@File: CellPhone.py
@Description: The Cellphone
@author: Tapio Koskinen

"""

class CellPhone:

	def __init__(self):
		self.__manufact = "Nokia"
		self.__model = "3310"
		self.__retailPrice = 20

	def set_manufact(self):
		self.__manufact = input("Set manufacturer: ")

	def set_model(self):
		self.__model = input("Set model: ")

	def set_retailPrice(self):
		self.__retailPrice = float(input("Set retail price: "))

	def get_manufact(self):
		return self.__manufact

	def get_model(self):
		return self.__model

	def get_retailPrice(self):
		return self.__retailPrice

	def __str__(self):
		return f"""\nManufacturer: {self.get_manufact()}
Model: {self.get_model()}
Retail price: {self.get_retailPrice()}"""

def main():

	my_phone = CellPhone()

	my_phone.set_manufact()

	my_phone.set_model()

	my_phone.set_retailPrice()

	print("Here is the data that you provided:",my_phone)

	my_phone.set_manufact()

	my_phone.set_model()

	my_phone.set_retailPrice()

	print("Here is the data that you provided:",my_phone)

main()



