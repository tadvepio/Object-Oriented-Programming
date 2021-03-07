# Class card
# Author: Tapio Koskinen
# Source: https://medium.com/@anthonytapias/build-a-deck-of-cards-with-oo-python-c41913a744d3).

class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val
    
    def show_card(self):
        print(f"{self.value} of {self.suit}")
    
    def __str__(self):
        return f"{self.value} of {self.suit}"