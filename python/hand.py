from deck import Deck
from card import Card

class Hand:

    def __init__(self, size, deck):
        self.hand = []
        for _ in range(size):
            self.hand.append(deck.cards[0])
            deck.cards.pop(0)

    def __str__(self):
        hand_string = ""
        for card in self.hand:
            hand_string += str(card)
        return hand_string