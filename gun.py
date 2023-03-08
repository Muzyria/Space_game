import pygame


class Gun:

    def __init__(self, screen):
        """init gun"""
        self.screen = screen
        self.image = pygame.image.load('images/gun.png')
        self.rect = self.image.get_rect()

