import pygame
import sys
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_state, log_event
from shot import Shot

def main():
    print(f"\nStarting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pyClock = pygame.time.Clock()
    dt = 0
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)
    player1 = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player1):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        for obj in asteroids:
            for shot in shots:
                if obj.collides_with(shot):
                    log_event("asteroid_shot")
                    obj.kill()
                    shot.kill()

        screen.fill("black")
        for items in drawable:
            items.draw(screen)
        pygame.display.flip()
        dt = pyClock.tick(60)/1000


        #print(f"time: {dt}")



if __name__ == "__main__":
    main()
