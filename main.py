import pygame
from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfield import *
from circleshape import CircleShape
import sys

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

Clock = pygame.time.Clock()
dt = 0

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
AsteroidField.containers = (updatable)

x = SCREEN_WIDTH / 2
y = SCREEN_HEIGHT /2
player = Player(x, y)
asteroid_field = AsteroidField()
    
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        clock_tick = Clock.tick(60)
        dt = clock_tick / 1000
        for item in drawable:
            item.draw(screen)
        updatable.update(dt)
        for item in asteroids:
            if CircleShape.collisions(item, player):
                sys.exit("Game over!")   
        pygame.display.flip()
        
        
   # print("Starting Asteroids!")
   # print(f"Screen width: {SCREEN_WIDTH}")
   # print(f"Screen height: {SCREEN_HEIGHT}")


if __name__=="__main__":
    main()


