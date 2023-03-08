import pygame


class Ino(pygame.sprite.Sprite):
    """clss one ino"""
    def __init__(self, screen):
        """init star pose"""
        super(Ino, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """output no on screen"""
        self.screen.blit(self.image, self.rect)