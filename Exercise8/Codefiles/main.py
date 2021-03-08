# Exercise 8
# Author: Tapio Koskinen
# Main for task 1

import flat

def main():

    my_flat = flat.Flat()
    print("\nInitial state(1) of my house:\n")
    print(my_flat)

    print("\nLets wash the windows and make the bed!")

    my_flat.set_windows("Washed")
    my_flat.set_bed("Made")

    print("\nState 2:\n")
    print(my_flat)

    print("\nLets dust the surfaces and vacuum the floors!")

    my_flat.set_surface("Dusted")
    my_flat.set_floors("Vacuumed")

    print("\nState 3:\n")
    print(my_flat)

    print("\nLets go shop for food and toiletpaper!")
    
    my_flat.set_fridge("Full of food")
    my_flat.set_toilet_paper("Enough")

    print("\nState 4:\n")

    print(my_flat)

    print("\nHmm, better get more toiletpaper. Just to make sure...")

    my_flat.set_toilet_paper("More than enough")

    print("\nState 5:\n")

    print(my_flat)

main()