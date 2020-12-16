import pygame


class Settings:

    """A class to sotre  all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (207, 221, 221)

        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 9.0
        self.bullet_width = 650
        self.bullet_height = 15
        self.bullet_color = (20, 25, 28)
        self.bullet_allowed = 3

        # Alien settings
        self.alien_speed = 22
        self.fleet_drop_speed = 12
        
        # fleet direction of 1 represent right; -1 represents left.
        self.fleet_direction = 1

    def fullscreen_settings(self):

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height


