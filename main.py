import pygame
import time
import random

WIDTH, HEIGHT = 100, 800 #pixels
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SpaceShit")

def main():
    run = True
    while(run):
        #quitting function
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

    pygame.QUIT


#this makes sure that the game is only run
#in case its not imported
if __name__ == "__main__":
    main()