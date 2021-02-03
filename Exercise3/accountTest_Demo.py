"""
Author: Tapio Koskinen
file: accountTest_demo.py
Date: 25.1.2021
Description: The bankAccount class simulates a bank account.
	# balance is private
	# two files
"""
import Bank_account_demo


def main():

	print('Hello')

	#Get the starting balance
	start_bal = float(input("Enter the starting balance: "))

	# Get the owner
	owner = input("Enter the owner: ")

	#Create a BankAccount object
	savings = Bank_account_demo.BankAccount(start_bal, owner)

	#Display the balance
	print(savings)

	#Get the amount to deposit
	amount = float(input('Enter the amount to be deposited: '))
	savings.deposit(amount)

	#Display the balance
	print(savings)

	#Get the balance to withdraw
	amount = float(input('Enter the amount to be withdrawn: '))
	savings.withdraw(amount)

	#Display the balance
	print(savings)


main()