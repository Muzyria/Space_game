import pygame, sys
from bullet import Bullet


def events(screen, gun, bullets):
    """evens obrabotka"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # right
            if event.key == pygame.K_RIGHT:
                gun.mright = True
            elif event.key == pygame.K_LEFT:
                gun.mleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)

        elif event.type == pygame.KEYUP:
            # right
            if event.key == pygame.K_RIGHT:
                gun.mright = False
            elif event.key == pygame.K_LEFT:
                gun.mleft = False


def update(bg_color, screen, gun, bullets):
    """update screen """
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    pygame.display.flip()


def update_bullets(bullets):
    """update pose bullets"""
    bullets.update()
    for bullet in bullets:
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
