import random
from card import Card

class Deck:
    def __init__(self):
        self.cards = []
        self.create()

    def create(self):
        for _ in range(1):
            for val in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13):
                for suit in ("H", "S", "C", "D"):
                    self.cards.append(Card(val, suit))

    def shuffle_deck(self):
        random.shuffle(self.cards)
        print("shuffling cards...")

    def __str__(self):
        deck_string = ""
        deck = self.cards
        for card in deck:
            deck_string += str(card)
        return deck_string