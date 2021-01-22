#Exercise 2 - Part 3
#Tapio Koskinen

asking = True
while asking:
	try:
		number_of_exercises = int(input("How many exercises did you do: "))
		break
	except ValueError:
		continue
	

grade_book = {9:1,10:2,11:3,12:4,13:5}

if number_of_exercises < 9:
	print("You did not pass the course")
elif number_of_exercises > 13:
	print("Your grade is 5")
else:
	print("Your grade is:",grade_book[number_of_exercises])
	