import sys

from settings import Settings
from ship import Ship
from bullet import Bullet

import pygame


class AlienInvasion:
    """General class to manage game assets and operation."""

    def __init__(self):
        """Initialize the game, create game resources."""
        pygame.init()
        self.settings = Settings()

        pygame.font.init()
        self.myfont15 = pygame.font.SysFont("Comic Sans MS", 15)

        #self.screen = pygame.display.set_mode((1000, 600))
        self.screen = pygame.display.set_mode((0,0 ), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(
            self
        )  # the required argument for Ship, which is self here refers to the current instance of AlienInvasion

        self.bullets = pygame.sprite.Group()
        # Set the background color.
        self.bg_color = (248, 10, 75)

        self.clock = pygame.time.Clock()

    def run_game(self):
        """Start the main loop for the game."""
        global start_time  # to make it available for the _update_screen method
        start_time = 0
        while True:
            # Watch for keyboard and mouse events.

            self._check_events()
            self.ship.update() #Ship position update after keyboard event check and before screen update.
            self.bullets.update() #Updates the position of the bullet.
            self._update_screen()

            time_used = self.clock.tick(30)
            start_time += time_used / 1000

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
                print(event.key)
                
                    # Move the ship to the right.
                self.ship.rect.x += 1
               
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
            

    def _check_keydown_events(self, event):
        """Respond to key presses"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Responds to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


    def display_time(self, time_elapsed):
        self.time_display = str(int(time_elapsed * 10) / 10)
        self.display = self.myfont15.render(
            f"Time elapsed : {self.time_display} seconds", 1, (0, 0, 0)
        )
        self.screen.blit(self.display, (20, 20))

    def instruct(self):
        self.label = self.myfont15.render(
            "Avoid The Aliens and Shoot to kill them", 1, (255, 0, 0)
        )
        self.screen.blit(self.label, (20, 550))

    def _update_screen(self):
        """Update images on the screen, and flip to the new screeen.
        Everything to be displayed on the screen should be between the screen fill and display_flip methods."""

        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()  # makes ship appear on top of background

        self.instruct()
        self.display_time(start_time)
        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == "__main__":
    # Make game intance and run the game.
    ai = AlienInvasion()
    ai.run_game()
