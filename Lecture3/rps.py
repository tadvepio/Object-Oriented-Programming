# File: rps.py
# Author: Tapio Koskinen
# Description: Main file for rock paper scissors

import random

import cookie_demo as cookie

def main():
	#print("Hello")

	choises = ["rock","paper","scissors"]
	cookie_shape = random.choice(choises)

	print("Cookie shape:",cookie_shape)

	cookie_flavor = input("Choose a flavor: ")
	print("Cookie flavor will be:", cookie_flavor)


	# Create a cookie object and initialize it with shape and flavor
	my_cookie = cookie.Cookie(cookie_shape, cookie_flavor)

	# Lets see what my cookie's state is:
	print(my_cookie)

	print("Booooring....")
	cookie_flavor = input("Change flavor to: ")
	cookie_shape = input("Change shape to: ")

	my_cookie.set_flavor(cookie_flavor)
	my_cookie.set_shape(cookie_shape)

	print("\nHere is your new cookie, enjoy.\n")
	print(my_cookie)

	print("I just want to see the shape.")
	print(my_cookie.get_shape())



main()