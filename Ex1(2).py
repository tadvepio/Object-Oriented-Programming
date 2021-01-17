#Part 7

def ap_counter(your__number):
	ap_numbers = []
	your__number -= your__number % 2
	
	for i in range(2, your__number+2, 2):
		ap_numbers.append(i)

	return ap_numbers

def sum_of_ap(your_ap):
	
	return sum(your_ap)

def sum_of_squared_ap(your_ap):

	the_squared_sum = 0
	for i in your_ap:
		the_squared_sum += i**2

	return the_squared_sum

def main():

	asking = True
	while asking:
		try:
			user_input = int(input("Slap a number on me: "))
			asking = False
		except ValueError:
			print("Only number please")

	ap_list = ap_counter(user_input)

	print("The arithemtic progression(2) from your number is:",ap_list)
	print("The sum of those numbers is",sum_of_ap(ap_list))
	print("The sum of squared terms in progression is",sum_of_squared_ap(ap_list))


main()