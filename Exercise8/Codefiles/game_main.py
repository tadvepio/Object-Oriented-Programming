# Exercise 8(and7), task 5
# A geoquiz where the user is asked for the capital of a country.
# Author: Tapio Koskinen

import player
import random

def main():

    user = player.Player("Tapio")

    game = True
    while game:

        # Open up a text file containing countries and capitals.
        f = open('country_capital.txt', 'r')

        # Python reads "-" as  â€ for some reason, so split the with that and add all to a list.
        country_capital = [line.split(" â€” ") for line in f]

        f.close()

        # Strip the "\n" from the capitals with .rstrip()
        for i in range(len(country_capital)):
            x = country_capital[i][1].rstrip('\n')
            country_capital[i][1] = x
        
        # Create a dictionray with the new list
        cou_cap = {}
        for i in range(len(country_capital)):
            cou_cap[country_capital[i][0]] = country_capital[i][1]

        try:

            game_mode = int(input("\n1. Play game\n2. Train\n3. Quit\n(1/2/3): "))
            if game_mode == 1 or game_mode == 2:
                # Create a game specific list
                game_countries = []

                # Add 10 random countries from the dictionary and pop from dict to prevent
                # duplicates
                for i in range(10):
                    y = random.randint(0,len(country_capital)-1)
                    game_countries.append(country_capital[y][0])
                    country_capital.pop(i)

                print("Time to play geoquiz! Guess the capital of a country!")
                score = 0
                # Ask 10 questions via a for loop
                for i in range(10):
                    print("\nQuestion",i+1)
                    answer = input(f"What is the capital of {game_countries[i]}\n")
                    if answer == cou_cap[game_countries[i]]:
                        # Check if the user is training or playing the real game
                        if game_mode == 1:
                            score += 1
                            user.set_score(score)
                        elif game_mode == 2:
                            score += 1
                            user.set_practice_score(score)
                    else:
                        continue
                
                print("\nResults:\n",user)
            
            elif game_mode == 3:
                game = False
            else:
                continue
        except ValueError:
            print("\nUse the numbers 1, 2 or 3")


main()