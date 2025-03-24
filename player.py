from circleshape import CircleShape
import pygame
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
from shot import Shot
# from main import screen

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
        
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        self.screen = screen
        return pygame.draw.polygon(
            screen, 
            (255, 255, 255), 
            self.triangle(), 
            2
            )
        
    def rotate(self, dt):
        self.dt = dt
        self.rotation -= PLAYER_TURN_SPEED * dt
        return self.rotation
    
    def rotate_counter(self, dt):
        self.dt = dt
        self.rotation += PLAYER_TURN_SPEED * dt
        return self.rotation
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt)
        if keys[pygame.K_d]:
            self.rotate_counter(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move_backwards(dt)
            
        if self.timer > 0:
            self.timer -= dt
        if self.timer < 0:
            self.timer = 0             
        if keys[pygame.K_SPACE] and self.timer == 0:
            self.shoot()
            self.timer = PLAYER_SHOOT_COOLDOWN

            
            
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        
    def move_backwards(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position -= forward * PLAYER_SPEED * dt
        
    def shoot(self):
        shot = Shot(self.position[0], self.position[1])
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        shot.velocity = forward * PLAYER_SHOOT_SPEED
        return shot
        