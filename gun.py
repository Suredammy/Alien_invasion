import pygame

class Gun:

    """A class that manage the shooting gun"""
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings
        #load the ship 

        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        #Start each new ship at the left center of the screen.
        self.rect.midleft = self.screen_rect.midleft

        #Store a decimal value for the gune vertical position.
        self.y = float(self.rect.y)

        #movement flag
        self.moving_up = False
        self.moving_down = False


    def draw_gun(self):
        """Draw the gun"""
        self.screen.blit(self.image, self.rect)
