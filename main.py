import pygame
from constants import *
from player import Player

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    time = pygame.time.Clock()

    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)

    while(1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return



        player.update(dt)

        screen.fill(color=(0,0,0))
        player.draw(screen)

        pygame.display.flip()

        time.tick(60)

        dt = time.tick(60) / 1000

if __name__ == "__main__":
    main()
