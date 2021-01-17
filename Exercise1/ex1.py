import random

#Object oriented programming
#Exercise 1
#Tapio Koskinen

#Part 1.

print("Hello world!")

#Part 2

#Create two empty lists for strings and numbers

number_list = [0 for i in range(10)]

string_list = ["" for i in range(10)]


#First we ask the user to give numbers for the "empty" slots with a for loop

"""for i in range(len(number_list)):
	handler = int(input("Give me a number for the "+str(i+1)+" item in number list: "))
	number_list[i] = handler
"""
#Next we do the same for the string list

for i in range(len(string_list)):
	handler = input("Give me a string for the "+str(i+1)+" item in string list: ")
	string_list[i] = handler

#Print out the new lists

#print("Your numberlist:",number_list,"\nYour stringlist:",string_list)

#Replace the numberlist with randomly generated numbers

for i in range(len(number_list)):
	number_list[i] = random.randint(0,99)

#Print out the new numberlist with random numbers
print("Numberlist with random numbers:",number_list)

#Part 3

#The simplest way to do this is to use pythons own sort() function

number_list.sort()
string_list = sorted(string_list, key=str.casefold)

print("Sorted numberlist in ascending order:",number_list)
print("Sorted stringlist in ascending order",string_list)



