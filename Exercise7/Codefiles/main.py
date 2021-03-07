# File:         main.py
# Author:       Tapio Koskinen
# Description:  Deck of cards and card games.

import card
import deck
import player

def main():
    
    print("Let's test that a single card works...")
    
    my_card = card.Card("Hearts", 12)
    my_card.show_card()
    print(my_card)

    print("Single card testing is over.\n")

    print("Let's test that a deck of card is created...")

    my_deck = deck.Deck()
    my_deck.show_deck()

    print("Card deck testing is over.\n")

    print("Let's shuffle the deck.")
    my_deck.shuffle_deck()

    print("Let's test that a deck of card is shuffled...")

    my_deck.show_deck()

    print("Cards should be suffled now.\n")

    print("Let's draw 2 cards and show them.")
    print("You draw:")
    card1 = my_deck.draw_card()
    card1.show_card()
    # Modified card1 to card2 so I can place them back.
    # Sorry for breaking the rules.
    print("Your opponent draw:")
    card2 = my_deck.draw_card()
    card2.show_card()
    
    # Code your Exercise 7 taks 4 game here. 

    # a. Draw 3 cards, highest value wins. Announce results (have clear output print). 
    # Hopefully have a re-draw if there are ties.

    print("\nLets draw 3 cards and see which one is the highest!")

    # Put the cards back and shuffle it
    my_deck.cards.append(card1)
    my_deck.cards.append(card2)
    my_deck.shuffle_deck()
    
    # Draw 3 cards and see wich one is highest
    playing = True
    while playing:
        three_cards = [my_deck.draw_card() for i in range(3)]
        # Show the cards
        print("The draws:")
        for j in three_cards:
            j.show_card()
        # Sort the objects with the sort method and inline lambda function
        # by the value of the cards
        three_cards.sort(key=lambda x: x.value, reverse=True)
        # Check if the highest card is bigger than the second
        if three_cards[0].value > three_cards[1].value:
            print("\nThe highest value card is:")
            three_cards[0].show_card()
            break
        # Tie. Put the cards back and reshuffle
        else:
            print("Tie. Reshuffle...\n")
            for c in three_cards:
                my_deck.cards.append(c)
                my_deck.shuffle_deck()

    # b. Implement card game Twenty-one (= Ventti in Finnish) or 
    # Blackjack for as many players as you like. Announce results clearly.
    # Notice, you do not necessarily need a Player class in 
    # this game (but you are allowed to have it).

    print("\n Time to play blackjack!")

    # Get the players
    getting_players = True
    player_dict = {}
    count = 0
    while getting_players:
        count += 1
        player_name = input("Player name: ")
        player_dict[count] = player.Player(player_name)
        confirming = True
        while confirming:
            addmore = input("Add more players?(y or n) ")
            if addmore == "y":
                confirming = False
            elif addmore == "n":
                confirming = False
                getting_players = False
            else:
                print("Use the keys y or n.")                  
    for key in player_dict:
        print("Player",key,":",player_dict[key].name)

    # Lets make a new deck and shuffle it.
    dealer = player.Player("Dealer")
    new_deck = deck.Deck()
    new_deck.shuffle_deck()
    print("Lets begin!")

    # Start the gameloop
    blackjack = True
    while blackjack:
        
        # Draw 2 cards for dealer
        dealer.draw(new_deck)
        dealer.draw(new_deck)
        # Deal the initial 2 cards for everyone
        for key in player_dict:
            player_dict[key].draw(new_deck)
            player_dict[key].draw(new_deck)
        
        # Let each player play their turn
        for key in player_dict:
            # Check the sum
            sum = 0
            for n in player_dict[key].hand:
                    if n.value >= 10:
                        sum += 10
                    else:
                        sum += n.value
            single_round = True
            # Start hit or stay
            while single_round:
                dropped_players_list = []
                print("Dealer card: ",dealer.hand[0])
                print(player_dict[key].name+"'s hand:")
                player_dict[key].showHand()
                print(sum)
                if sum == 21:
                    print("Blackjack! You win!")
                    dropped_players_list.append(key)
                    single_round = False
                elif sum > 21:
                    print("Bust! You lose!")
                    dropped_players_list.append(key)
                    single_round = False
                else:
                    asking = True
                    while asking:
                        hit_or_stay = input("\nHit or stay?(h/s)")
                        if hit_or_stay == "h":
                            player_dict[key].draw(new_deck)
                            sum += player_dict[key].hand[-1].value
                            asking = False
                        elif hit_or_stay == "s":
                            asking = False
                            single_round = False
                        else:
                            print("\nUse the key h or s")
        
        # Time for the dealer to play
        house_play = True
        while house_play:
            print("\nDealers hand:")
            dealer.showHand()
            print("Sum:",dealer.getSum())
            dealer_sum = dealer.getSum()
            if dealer_sum < 17:
                dealer.draw(new_deck)
            else:
                house_play = False
        
        # Check who wins and loses
        for p in dropped_players_list:
            player_dict.pop(p)
        if dealer_sum == 21:
            print("Dealer wins.")
            dealer.showHand()
            print("Sum: ",dealer.getSum())
        elif dealer_sum > 21:
            print("Dealer busts. Players win")
        else:
            for key in player_dict:
                your_sum = player_dict[key].getSum()
                if your_sum > dealer_sum:
                    print(player_dict[key].name,"wins the dealer!")
                elif your_sum < dealer_sum:
                    print("Dealer beats",player_dict[key].name)
                else:
                    print("Tie between dealer and",player_dict[key].name)

        break

                

# Calling the main function here, do not change...
main()
