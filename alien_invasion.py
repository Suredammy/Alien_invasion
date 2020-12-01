import sys

from settings import Settings

import pygame


class AlienInvasion:
    """General class to manage game assets and operation."""

    def __init__(self):
        """Initialize the game, create game resources."""
        pygame.init()

        self.screen = pygame.display.set_mode((1000, 600))
        pygame.display.set_caption("Alien Invasion")

        #Set the background color.
        self.bg_color = (225, 225, 225)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            #Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)

            # Make the most recently drawn screen visible.
            pygame.display.flip()


if __name__ == "__main__":
    # Make game intance and run the game.
    ai = AlienInvasion()
    ai.run_game()
