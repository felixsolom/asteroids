import pygame
from constants import *
from player import Player

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

Clock = pygame.time.Clock()
dt = 0

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
Player.containers = (updatable, drawable)

x = SCREEN_WIDTH / 2
y = SCREEN_HEIGHT /2
player = Player(x, y)
    
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
        pygame.display.flip()
        
        
   # print("Starting Asteroids!")
   # print(f"Screen width: {SCREEN_WIDTH}")
   # print(f"Screen height: {SCREEN_HEIGHT}")


if __name__=="__main__":
    main()


