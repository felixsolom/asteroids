from circleshape import CircleShape
import pygame

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)       
        
    def draw(self, screen):
        self.screen = screen
        return pygame.draw.circle(
            screen, 
            (255, 255, 255), 
            self.position, 
            self.radius, 
            2
            )