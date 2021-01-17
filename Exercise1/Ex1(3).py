#Part 8

import random

def choose_number():
	choosing = True
	while choosing:
		try:
			user_choise = int(input("Choose by typing the number Rock(1), Paper(2) or Scissors(3): "))
			if user_choise < 1 or user_choise > 3:
				print("Choose the number 1, 2 or 3")
			else:
				choosing = False
		except ValueError:
			print("Choose the number 1, 2 or 3")
	return user_choise

def check_score(score):
	for key in score:
		if score[key] >= 3:
			return key

def play_again():
	global Score
	choosing = True
	while choosing:
		try:
			play_again = int(input("Play again? yes=1 no=2: "))
			if play_again == 1:
				Score = {"Player":0,"Machine":0}
				return True
			elif play_again == 2:
				return False
			else:
				print("1 or 2")
		except ValueError:
			print("1 or 2")


def main():

	the_game = True

	while the_game:

		print("Lets play rock paper scissors! Best out of three!")

		playing = True

		weapons = ["filler", "Rock", "Paper", "Scissors"]

		Score = {"Player":0,"Machine":0}

		while playing:

			player = choose_number()

			machine = random.randint(1,3)

			if player == machine:
				print("Tie!")

			elif player == 1:
				if machine == 2:
					print("You lose.",weapons[machine],"beats",weapons[player],".")
					Score["Machine"] += 1
				elif machine == 3:
					print("You win!",weapons[player],"beats",weapons[machine],".")
					Score["Player"] += 1
			elif player == 2:
				if machine == 1:
					print("You win!",weapons[player],"beats",weapons[machine],".")
					Score["Player"] += 1
				elif machine == 3:
					print("You lose.",weapons[machine]," beats",weapons[player],".")
					Score["Machine"] += 1
			elif player == 3:
				if machine == 1:
					print("You lose.",weapons[machine],"beats",weapons[player],".")
					Score["Machine"] += 1
				elif machine == 2:
					print("You win!",weapons[player],"beats",weapons[machine],".")
					Score["Player"] += 1

			if check_score(Score) == "Machine":
				print("Machine won 3 times. You lose.")
				playing = False
			elif check_score(Score) == "Player":
				print("You won 3 times! You win the game!")
				playing = False
	
		the_game = play_again()

	print("Thanks for playing!")

main()