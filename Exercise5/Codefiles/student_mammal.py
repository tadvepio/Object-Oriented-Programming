"""
Created 8.2.2021
@File: student_mammal.py
@Description: Create a dictionary with studen object as key
              and a pet mammal as value
@author: Tapio Koskinen

"""

# Import necessary modules
from mammal import Mammal
from student_class import Student

def main():

    # Create a dictionary to hold mammal and student
    # Numbered keys is the way.
    stud_pet_dic = dict()
    # Create a list to hold both student and mammal object
    stud_pet_lst = []

    # Create both objects and store them into the
    # empty list as a separate list, for convenience
    myself = Student("Tapio", "Koskinen", 1337)
    mypet = Mammal(1,"Bear","Tiny","Big",150,2)
    stud_pet_lst.append([myself,mypet])

    friend = Student("Matti","Mallikas", 100)
    friendpet = Mammal(2, "Unicorn", "Fred","Medium", 500, 1.5)
    stud_pet_lst.append([friend,friendpet])

    # Add each pair that is in the pair list
    for i in range(len(stud_pet_lst)):
        stud_pet_dic[i] = stud_pet_lst[i]

    # Loop through all key in the dictionary
    # and print out the student and their pet
    for i in stud_pet_dic:
        pair = stud_pet_dic[i]
        print("*"*40)
        print(f"Student:\n\n{pair[0]}\n"+"-"*30,f"\nHis/her pet:\n\n{pair[1]}")
    
    print("*"*40)

main()
