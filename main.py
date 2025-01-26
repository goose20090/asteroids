import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill(color=[0,0,0])

        for obj in drawable:
            obj.draw(screen) 
        
        for obj in updatable:
            obj.update(dt)
        
        for obj in asteroids:
            if obj.has_collided(player):
                print("Game Over!")
                sys.exit()

        pygame.display.flip()
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
