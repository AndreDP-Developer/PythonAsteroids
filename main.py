# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    pygame.init()
    # new GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #game loop
    while True:
        # allow exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return         
            
        #fill with black
        screen.fill((1,1,1))

        # display update
        pygame.display.flip()  

if __name__ == "__main__":
    main()
