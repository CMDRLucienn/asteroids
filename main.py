import pygame
from constants import *
from player import Player

def main():
    pygame.init()

    dt = 0
    phys_clock = pygame.time.Clock()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
        
        screen.fill(color=(0, 0, 0))

        for item in updatable:
            item.update(dt)   

        for item in drawable:
            item.draw(screen)

        pygame.display.flip()
        dt = phys_clock.tick(60) / 1000

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()