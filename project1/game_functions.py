import sys
import pygame

def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(ship, event)
        elif event.type == pygame.KEYUP:
            check_keyup_events(ship, event)

def check_keyup_events(ship, event):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_keydown_events(ship, event):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

def update_screen(game_settings, screen, ship):
    """Update and flip the screen"""
    screen.fill(game_settings.bg_color)
    ship.blit()
    pygame.display.flip()
