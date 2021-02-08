"""
Created 8.2.2021
@File: player_test.py
@Description: Creating a dictionary with player id
              as key and dice as value
@author: Tapio Koskinen

"""

from Dice_demo import Dice
from player_class import Player

# The point is that the function can take any
# amount of full names and return first names and 
# last names in separate lists, separated with a colon.
def name_sep(stringofnames):
    data = stringofnames
    fullnames = data.split(",")
    fnames = []
    lnames = []
    for i in range(len(fullnames)):
        separated = fullnames[i].split(" ")
        fnames.append(separated[0])
        lnames.append(separated[1])
    return fnames,lnames

def main():

    # Pretending there is some input data that
    namestring = "Michael Jackson,Janice Joplin,Tina Turner,Billy Joel"    
    # Calling the previous function
    listed_and_separated = name_sep(namestring)
    # Create an empty player dictionary
    player_dictionary = dict()
    # Loop through all names, I chose the first names, doesn't matter
    for i in range(len(listed_and_separated[0])):
        # Create a player class with a temporary variable name
        name = Player(listed_and_separated[0][i],listed_and_separated[1][i], i+1)
        # Add the id from the current player and add it to the dictionary as a key 
        # and assign a Dice instance as a value, with the name of the owner.
        player_dictionary[name.get_id()] = Dice(listed_and_separated[0][i])
    # Loop through keys, roll their dices and print the names
    # and the dices current values
    for key in player_dictionary:
        player_dictionary[key].roll()
        print(player_dictionary[key].get_owner(),player_dictionary[key].get_sideup())


main()



