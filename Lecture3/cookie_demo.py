# File: cookie_demo.py
# Author: Tapio Koskinen
# Description: Create cookies of different flavor and shape


# Cookie class

class Cookie:

	# Initialize data attribute
	# __shape and __flavor are data attributes
	# They are both private
	def __init__(self, init_shape, init_flavor):
		self.__shape = init_shape
		self.__flavor = init_flavor


	# Accessor methods (get), mutator methods (set)

	def set_shape(self, desired_shape):
		self.__shape = desired_shape

	def get_shape(self):
		return self.__shape

	def set_flavor(self, desired_flavor):
		self.__flavor = desired_flavor

	def get_flavor(self):
		return self.__flavor


	# Return the object state (= values of the data attributes)

	def __str__(self):
		return 'Your cookie is ' + format(self.__shape) + '-shaped and tastes like ' + format(self.__flavor) + '.'


