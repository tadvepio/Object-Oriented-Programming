"""
Author: Tapio Koskinen
file: Bank_account_demo.py
Date: 25.1.2021
Description: The bankAccount class simulates a bank account.
	# balance is private
	# two files
"""

class BankAccount:

	# The __init__ method accepts an argument for
	# the account's balance. It is assigned to
	# the __balance attribute
	def __init__(self, bal, owner):
		self.__balance = bal
		self.__owner = owner


	# The deposit method makes a deposit into the account
	def deposit(self, amount):
		#If the input is less than 0, print error message
		if amount > 0:
			self.__balance += amount
		else:
			print("Error: Cannot deposit negative money")


	# The withdraw method withdraws an amoutn from the account
	def withdraw(self, amount):
		if self.__balance >= amount:
			self.__balance -= amount
		else:
			print('Error: Insufficient funds.')


	# The get_balance method returns the account balance
	def get_balance(self):
		return self.__balance

	# The get_owner method returns the bank account owner
	def get_owner(self):
		return self.__owner

	# The __str__ method returns a string
	# indicating the objects
	def __str__(self):
		return f"""Balance: {self.__balance} Owner: {self.__owner}"""

