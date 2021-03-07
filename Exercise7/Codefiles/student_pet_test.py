# Task 5 UML diagram
# Author Tapio Koskinen

import student, pet

def main():

    tapio = student.Student("Tapio", "Koskinen", 1800509)
    musti = pet.Pet("Dog","Musti","Tapio")
    mimosa = pet.Pet("Cat","mimosa","Tapio")

    print("Test with empty")
    tapio.print_pets()
    tapio.add_pets(musti)
    print("After musti")
    print(tapio.print_pets())
    tapio.add_pets(mimosa)
    print("After mimosa")
    print(tapio.print_pets())

    print("Here is",tapio.get_first_name(),"and his pet(s):")
    print(tapio)


main()