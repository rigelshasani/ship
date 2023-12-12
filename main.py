import pygame
import time
import random

WIDTH, HEIGHT = 1080, 800 #pixels
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SpaceShit")
#
BG = pygame.transform.scale(pygame.image.load("andromeda.jpg"), (WIDTH, HEIGHT))

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
PLAYER_VEL = 5


def draw(player):
    #blit draws the surface
    WIN.blit(BG, (0,0))
    pygame.draw.rect(WIN, "red", player)
    #does this everytime there's a change
    pygame.display.update()

def main():
    run = True
    #this is the main loop

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, 
                         PLAYER_WIDTH, PLAYER_HEIGHT)
    clock = pygame.time.Clock()

    while(run):
        clock.tick(60)
        #here events are checked
        for event in pygame.event.get():
            #quitting function
            if event.type == pygame.QUIT:
                run = False
                break
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL
        draw(player)

    pygame.QUIT


#this makes sure that the game is only run
#in case its not imported
if __name__ == "__main__":
    main()