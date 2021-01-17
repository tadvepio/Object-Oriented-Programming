#Part 4

def negatives(your_numbers):
	negatives = 0
	for i in your_numbers:
		if i < 0:
			negatives += 1
		else:
			continue
	
	return negatives

#Part 5

def even_numbers(your_numbers):
	even_numbers = 0
	for i in your_numbers:
		if i % 2 == 0:
			even_numbers += 1
		else:
			continue
	return even_numbers

#Part 6

def sum_of_div_3(your_numbers):
	positive_div_threes = []
	for i in your_numbers:
		if i > 0:
			if i % 3 == 0:
				positive_div_threes.append(i)
			else:
				continue
		else:
			continue
	the_sum = sum(positive_div_threes)
	return the_sum

def main():
	
	integer_list = []
	handler = 0
	asking = True
	while asking:
		try:
			handler = int(input("Give me any number: "))
			if handler != 0:
				integer_list.append(handler)
			else:
				asking = False
		except ValueError:
			print("Only numbers please")
	
	#print("The number of negative numbers in list is:",negatives(integer_list))

	#print("The number of even numbers in list is:",even_numbers(integer_list))

	print("The sum of positive numbers divisible by 3 is", sum_of_div_3(integer_list))

main()