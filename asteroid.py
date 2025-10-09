import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        pass
    
    def draw(self, screen):
        pygame.draw.cirle(screen, "white", self.position, self.position, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt
    