#Part 5 - The average score
#Tapio Koskinen


#Create a function that creates a dictionary of students and
#their grades
def student_grade_dictionary():
	student_list = {}

	asking = True
	while asking:
		#Student name will be the key
		student = input("Student name:")
		#Student grade will be the value of current key
		student_list[student] = int(input("Grade:"))
		add_more = input("Add more?(y/n): ")
		if add_more == "y":
			continue
		elif add_more == "n":
			break
	#Return the created class
	return student_list

def average_grade(your_dict):
	#A placeholder for the sum of grades
	sum_of_grades = 0
	#Loop through all the students in the dictionary and
	#sum their grades
	for key in your_dict:
		sum_of_grades += your_dict[key]
	#The average will be the sum divided to the sum of students
	average = sum_of_grades/len(your_dict)
	#Return that value
	return average

def main():
	#Create your classroom
	print("Create your class with grades\n")
	my_students = student_grade_dictionary()
	#Print out the average grade of your classroom
	print("The average grade of this class is",average_grade(my_students))
#Run the program
main()
