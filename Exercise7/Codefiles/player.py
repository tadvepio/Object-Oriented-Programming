# class Player
# Author: Tapio Koskinen
# Source: https://medium.com/@anthonytapias/build-a-deck-of-cards-with-oo-python-c41913a744d3).

import deck, card

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
    
    def draw(self, deck):
        self.hand.append(deck.draw_card())
        return self
    
    def showHand(self):
        for card in self.hand:
            card.show_card()
    
    def getSum(self):
        sum = 0
        for card in self.hand:
            if card.value >= 10:
                sum += 10
            else:
                sum += card.value
        return sum
