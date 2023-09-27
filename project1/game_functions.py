import sys
import pygame

from bullet import Bullet

def check_events(game_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(game_settings, screen, ship, event, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(ship, event)

def check_keyup_events(ship, event):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_keydown_events(game_settings, screen, ship, event, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(game_settings, screen, ship, bullets)

def fire_bullet(game_settings, screen, ship, bullets):
    if len(bullets) < game_settings.bullets_allowed:
        new_bullet = Bullet(game_settings, screen, ship)
        bullets.add(new_bullet)

def update_screen(game_settings, screen, ship, bullets):
    """Update and flip the screen"""
    screen.fill(game_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    
    ship.blit()
    pygame.display.flip()

def update_bullets(bullets):
    bullets.update()
    # remove bullets that went out of screen
    for bullet in bullets.copy():
        if bullet.rect.bottom  <= 0:
            bullets.remove(bullet)
    #print(len(bullets))
