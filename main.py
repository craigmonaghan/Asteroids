import pygame
from constants import *
from asteroid import Asteroid
from player import Player

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroid = pygame.sprite.Group()

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Asteroid.containers = (asteroid, updatable, drawable)
    Player.containers = (updatable, drawable)    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        
        dt = clock.tick(60) / 1000
        updatable.update(dt)
        
        screen.fill((0, 0, 0))
        for sprite in drawable:
            sprite.draw(screen)
        
        pygame.display.flip()
        

if __name__ == "__main__":
    main()