# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shoot import *

def main():
    pygame.init()
    # new GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # 60 FPS
    clock = pygame.time.Clock()
    # delta
    dt = 0
    # create pygame groups
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shoot.containers = (shots, updateable, drawable)

    asteroidField = AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    #game loop
    while True:
        # allow exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return         
            
        #fill with black
        screen.fill((1,1,1))

        #move player
        for sprite in updateable:
            sprite.update(dt)
        player.move(dt)

        #draw player
        for sprite in drawable:
            sprite.draw(screen)

        #asteroids
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game Over!")
                exit()
            for shot in shots:
                if asteroid.collision(shot):
                    shot.kill()
                    asteroid.split()

        # 60 FPS (1/60th of a second)
        dt = clock.tick(60)
        dt /= 1000  # convert to second

        # display update
        pygame.display.flip()  

if __name__ == "__main__":
    main()
