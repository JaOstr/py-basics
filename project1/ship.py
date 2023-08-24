import pygame

class Ship():

    def __init__(self, game_settings, screen):
        """Init the space ship and its initial position"""
        self.game_settings = game_settings
        self.screen = screen
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the position"""
        if self.moving_right:
            self.center += self.game_settings.ship_speed_factor
        if self.moving_left:
            self.center -= self.game_settings.ship_speed_factor
        self.rect.centerx = self.center
    
    def blit(self):
        """Show the space ship at its current position"""
        self.screen.blit(self.image, self.rect)
