import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    
    def draw(self, screen):
        return pygame.draw.circle(screen, (self.x, self.y), self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)