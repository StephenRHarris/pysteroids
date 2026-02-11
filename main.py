import pygame
from constants import *
from logger import log_state
def main():
    print(f"\nStarting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pyClock = pygame.time.Clock()
    dt = 0
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        dt = pyClock.tick(60)/1000
        #print(f"time: {dt}")
        pygame.display.flip()



if __name__ == "__main__":
    main()
