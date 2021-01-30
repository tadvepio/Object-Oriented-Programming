# Author: Tapio Koskinen
# File: dice_game.py
# Date: 30.1.2021
# Description: Exercise 3 - part 7

# Import the Dice

import Dice_demo

def main():

	#Assign dices with owners to 3 players

	player1 = Dice_demo.Dice("Steve")
	player2 = Dice_demo.Dice("John")
	player3 = Dice_demo.Dice("Alice")

	# First round variable for looping

	first_round = True

	# Make a list to keep track of players

	player_list = [player1,player2,player3]

	print("Time for a dice tournament!")

	# First round
	while first_round:

		# Throw for all player
		for i in player_list:
			i.roll()
		print(f"First round rolls:\n{player1.get_owner()}: {player1.get_sideup()}\nJohn: {player2.get_sideup()}\nAlice: {player1.get_sideup()}")

		# Set the initial value of smallest to player 1
		smallest = player1.get_sideup()

		# Set smallest to player2 if its smaller than smallest
		if player2.get_sideup() < smallest:
			smallest = player2.get_sideup()
			#If player 3 threw less, remove player3 from the game and end the round
			if player3.get_sideup() < smallest:
				player_list.remove(player3)
				first_round = False
			#If player 3 dice equals to the smallest, everyone throws again
			elif player3.get_sideup() == smallest:
				print("Roll again!")
				continue
			#Otherwise remove player2 from the game
			else:
				player_list.remove(player2)
				first_round = False

		# Run through checkups if p1 and p2 have same values
		elif player2.get_sideup() > smallest:
			if player3.get_sideup() >= smallest:
				print("Roll again!")
				continue
			else:
				player_list.remove(player1)
				first_round = False

	# Round 2 begins with remaining players
	round2 = True

	while round2:
		#Just to make it prettier
		p1 = player_list[0]
		p2 = player_list[1]

		# Roll
		p1.roll()
		p2.roll()

		# Announce players rolls using objects

		print(f"Second round rolls:\n{p1.get_owner()}: {p1.get_sideup()}\n{p2.get_owner()}: {p2.get_sideup()}")

		#Check for the winner

		if p1.get_sideup() > p2.get_sideup():
			print(f"{p1.get_owner()} wins!")
			round2 = False
		elif p1.get_sideup() == p2.get_sideup():
			continue
		else:
			print(f"{p2.get_owner()} wins!")
			round2 = False

main()
