import pygame
from constants import *
from player import *
from logger import log_state
def main():
    print(f"\nStarting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pyClock = pygame.time.Clock()
    dt = 0
    player1 = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        player1.update(dt)
        screen.fill("black")
        player1.draw(screen)
        pygame.display.flip()
        dt = pyClock.tick(60)/1000

        #print(f"time: {dt}")



if __name__ == "__main__":
    main()
