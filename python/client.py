import pygame
import os
import random
import time
import numpy
from card import Card
from deck import Deck
from hand import Hand

width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

clientNumber = 0

def main():
    clock = pygame.time.Clock()

    display_dim = (800, 600)
    #background = pygame.image.load(os.path.join("assets", "background.jpg"))
    #background = pygame.transform.scale(background, display_dim)


    gameDisplay = pygame.display.set_mode(display_dim)

    #print(pygame.display.Info())
    run = True
    d = Deck()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        c = d.cards[0]
        print(c)
        d.shuffle_deck()
        gameDisplay.fill((255, 255, 255))

        c.face = pygame.transform.scale(c.face, (150,250))

        #gameDisplay.blit(background, (0,0)) 

        gameDisplay.blit(c.face, (50, 50))

        #gameDisplay.blit(test,(50, 50))

        time.sleep(1)
        pygame.display.update()

        clock.tick(60)


if __name__ == "__main__": main()