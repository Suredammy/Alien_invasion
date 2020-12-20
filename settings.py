import pygame
from button import Button as bt

class Settings:

    """A class to sotre  all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (207, 221, 221)
        self.play_level = 1
        # Ship settings
        
        self.ship_limit = 3

        # Bullet settings
        
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (20, 25, 28)
        #self.bullet_allowed = 10

        # Alien settings
        
        self.fleet_drop_speed = 1

        #How quickly the game speeds up
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings(self.play_level)

    def initialize_dynamic_settings(self, play_level):
        self.play_level = play_level
        self.play_speed = self.speedup_scale ** (play_level -1)
        self.ship_speed = 2 * self.play_speed
        self.bullet_speed = 2 * self.play_speed
        self.alien_speed = 2 * self.play_speed
        self.bullet_allowed = 3 + (3 * (self.play_level -1))
        

        # Scoring
        self.alien_points = int(50 * self.score_scale ** (self.play_level -1))
        self.bullet_points = int(-20 * self.score_scale ** (self.play_level-1))


        # fleet direction of 1 represent right; -1 represents left.
        self.fleet_direction = 1


    def fullscreen_settings(self):

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.bullet_allowed += 3
    


