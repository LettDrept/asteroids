# This project was developed through Boot.dev's
# online Asteroids guided project 


# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame

from constants import *                     # imports variables from constants
from circleshape import *                   # imports base game shape
from player import *                        # imports the player's object
from asteroid import *                      # imports the asteroid objects
from asteroidfield import *                 # imports the field for all asteroids
from shot import *                          # imports the player's shots

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()            # initialize the clock before the main loop
    dt = 0                                 # delta time

    # Establish all the necessary pygame.sprite Groups
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    # Identify which groups objects belong to
    Player.containers = (updateable, drawable)
    Shot.containers = (shots, updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    
    the_player = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    the_field = AsteroidField()

    while True:
        for event in pygame.event.get():   # allows you to close the window
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))              # sets screen color to black

        updateable.update(dt)               # updates positions of all objects
        for asteroid in asteroids:          # checks for player collision with asteroids
           if asteroid.collision(the_player):
               print("Game over!")
               sys.exit()
        for asteroid in asteroids:          # if a player's shot hits an asteroid
            for shot in shots:
                if asteroid.collision(shot):
                    shot.kill()
                    asteroid.split()

        for drawable_object in drawable:    # redraws all objects
            drawable_object.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000         # sets rotation speed based on 60fps

    



if __name__ == "__main__":
    main()