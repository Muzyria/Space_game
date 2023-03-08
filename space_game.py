import pygame, controls
# import sys
from gun import Gun


def run():

    pygame.init() # инициализация игры
    screen = pygame.display.set_mode((700, 700))
    pygame.display.set_caption("My Space Game")
    bg_color = (0, 0, 0)
    gun = Gun(screen)

    while True:
        controls.events(gun)
        gun.update_gun()
        screen.fill(bg_color)
        gun.output()
        pygame.display.flip()



run()
