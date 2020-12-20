import sys

import pygame.font


class Button:
    def __init__(self, ai_game, msg, level):
        """Initialize button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.screen_width, self.screen_height = self.screen_rect.width, self.screen_rect.height
        self.level = level

        # Set the dimensions and properties of the button
        self.width, self.height = 250, 50 + self.level
        self.button_color = (5, 105, 9)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 32)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        
        self.rect.x = (self.screen_width - self.width) // 2
        self.rect.y = self.screen_rect.centery - (self.height * self.level) 


        # The button message needs to be prepped only once.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
            """Turn msg into a rendered image and center text on the button."""
            self.msg_image = self.font.render(
                msg, True, self.text_color, self.button_color
            )
            self.msg_image_rect = self.msg_image.get_rect()
            #self.msg_image_rect.center = self.rect.center   
            self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        #Draw blank button and then draw message.
        self.screen.fill(self.button_color, self.rect)   
        self.screen.blit(self.msg_image, self.msg_image_rect)









