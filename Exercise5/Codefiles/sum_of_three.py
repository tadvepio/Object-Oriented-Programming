"""
Created 8.2.2021
@File: sum_of_three.py
@Description: A game where three dices throw 3 times 
              and the biggest value wins. Ties go to sudden death.
@author: Tapio Koskinen

"""

import Dice_demo
import random

# Sums up three throws and takes the Dice class
# as a parameter.
def get_sum_of_three(d):
    sum = 0
    for i in range(3):
        d.roll()
        sum += d.get_sideup()
    return sum


def main():

    # Players in a list. Shuffle to get random players each time
    # The Dice class requires an owner when initialized
    Players = ["Jenny","Johnny","Sammy","Lizzie","Suzy"]
    random.shuffle(Players)

    # Create a list of dice objects randomly from 3 to 5
    dices = []
    for i in range(random.randint(3,5)):
        dices.append(Dice_demo.Dice(Players[i]))

    # Print the contestans
    print("Here are the players:")
    for i in range(len(dices)):
        dices[i].roll()
        print(dices[i].get_owner())
    
    print("\nRound one!")

    # Create scorelist to keep track of scores
    # The index numbers of score items are the same as the ones in dice list
    scores = []
    for i in range(len(dices)):
        # Append to the scorelist with the help of
        # previously created function
        scores.append(get_sum_of_three(dices[i]))

    # Print all the players and the sum of their 3 throws
    for i in range(len(dices)):
        print(dices[i].get_owner(),":",scores[i])

    # Takes a list as a parameter and returns
    # a new list containing the indexes of highest
    # values from the original list
    def roller(s):
        # Get the biggest value of the input list
        highscore = max(s)
        # Create a list for returning the maximum values
        checklist = []
        # variable j is to keep track of the index
        # of the element from the original input
        j = 0
        # if an element from the input list is equal
        # to the maximum value, add it to the checklist
        for i in s:
            if i == highscore:
                checklist.append(j)
            # For iterating purposes
            # add 1 to keep track
            j += 1
        # Return the indexes of the highest values
        return checklist
    
    # Get a list of players with
    # highest values(indexes for dice list)
    finalists = roller(scores)

    # If there is a tie between dices, 
    # go for sudden death
    if len(finalists) > 1:
        print("\nRound two!")
        finaling = True
        # A little variable to check how
        # many times finalists rerolled
        rolls = 1
        while finaling:
            # Create a helping list
            # to keep track of last round
            # scores
            last_scores = []
            # Roll each dices once
            for index in finalists:
                dices[index].roll()
                last_scores.append(dices[index].get_sideup())
            # Checking list is to see if there still are multiple
            # top scores
            checking = roller(last_scores)
            # Print the finalists and their rolls
            for i in finalists:
                print(dices[i].get_owner(),":",dices[i].get_sideup())
            # If there are ties, start over
            if len(checking) > 1:
                rolls += 1
                continue
            # Else, print out the winner
            else:
                winner = [dices[finalists[checking[-1]]]]
                print("\nAfter",rolls,"roll(s)",winner[0].get_owner(),"emerged victorious!")
                break
    # Print out the winner if there were no ties
    else:
        print("\nThe winner is:",dices[finalists[0]].get_owner())

    # 117 might be overkill
main()