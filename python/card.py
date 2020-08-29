import os
import pygame
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.face = pygame.image.load(os.path.join("assets", str(self.value) + self.suit + ".png"))
        self.back = pygame.image.load(os.path.join("assets", "Gray_back.jpg"))

    def __str__(self):
        return "Card value: " + str(self.value) + " suit: " + str(self.suit) + "\n"