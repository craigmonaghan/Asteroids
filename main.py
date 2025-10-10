import pygame
import sys

from constants import *
from asteroid import Asteroid
from player import Player
from asteroidfield import AsteroidField
from shot import Shot

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Player.containers = (updatable, drawable) 
    Shot.containers = (updatable, drawable, shots)   
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        
        dt = clock.tick(60) / 1000
        updatable.update(dt)
        
        screen.fill((0, 0, 0))
        for sprite in drawable:
            sprite.draw(screen)
        
       
        shots_to_kill = []
        asteroid_to_kill = []
        
        for asteroid in asteroids:
            if player.is_colliding(asteroid):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if shot.is_colliding(asteroid):
                    shots_to_kill.append(shot)
                    asteroid_to_kill.append(asteroid)
        
        for shot in shots_to_kill:
            shot.kill()
        for asteroid in asteroid_to_kill:
            asteroid.split()
        pygame.display.flip()
        

if __name__ == "__main__":
    main()