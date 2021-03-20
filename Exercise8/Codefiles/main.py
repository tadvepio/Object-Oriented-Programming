# Exercise 8
# Author: Tapio Koskinen
# Main for task 1

import flat
import cookie
import random

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

    # Task 3: Cookie

    # Create cookies with random flavors and then bake them.

    print("*"*20)
    print("Time to bake some cookies! Lets make 10!")

    cookies = {}
    for i in range(10):
        cookies[i+1] = cookie.Cookie("Round")
        cookies[i+1].set_random_flavor()
        cookies[i+1].set_baked()
    
    # Print all cookies

    for key in cookies:
        print("\n")
        print(cookies[key])

    # Frost the new 10 cookies

    print("\nLets frost those badboys!")

    for key in cookies:
        cookies[key].set_frosted()

    # Print all cookies

    for key in cookies:
        print("\n")
        print(cookies[key])

    # Ask the user if his/her flavor is present. If not, create a new cookie.

    checking = True
    while checking:
        check_flavor = input("\nIs your favorite flavor present?(y/n) ")
        if check_flavor == "y":
            break
        elif check_flavor == "n":
            fav_flav = input("\nWhats your favorite flavor: ")
            cookies[len(cookies)+1] = cookie.Cookie("Round", fav_flav)
            cookies[len(cookies)].set_baked()
            cookies[len(cookies)].set_frosted()
            break
        else:
            print("\nUse the key y or n.")

    # Print all cookies.

    for key in cookies:
        print("\n")
        print(cookies[key])

    

main()