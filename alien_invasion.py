import sys
from time import sleep
from random import randint

import pygame

from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from gun import Gun
from alien import Alien





class AlienInvasion:
    """General class to manage game assets and operation."""

    def __init__(self):
        """Initialize the game, create game resources."""
        pygame.init()
        self.settings = Settings()

        pygame.font.init()
        self.myfont15 = pygame.font.SysFont("Comic Sans MS", 15)

        self.screen = pygame.display.set_mode((1200, 700))

        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")

        #Create an instance to store game statistics.
        self.stats = GameStats(self)

        self.ship = Ship(
            self
        )  # the required argument for Ship, which is self here refers to the current instance of AlienInvasion

        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Set the background color.
        self.bg_color = (248, 10, 75)

        self.clock = pygame.time.Clock()
        self.start_time = 0

        # Start Alien Invasion in an active state.
        self.stats.game_active = True

    def run_game(self):
        """Start the main loop for the game."""
        
        while True:
            
            
            # Watch for keyboard and mouse events.

            self._check_events()
            if self.stats.game_active:
                
                self.ship.update()  # Ship position update after keyboard event check and before screen update.
                self._update_bullets()
                self._update_aliens()
            self._update_screen()

            

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

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
        elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
            sys.exit()

        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Responds to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Make an alien.
        # Create one instance of alien and add it to the group that will hold the fleet
        # Create an alien and find the number of aliens in a row.
        # Spacing between each alien is equal to half alien width.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (1.8 * alien_width)

        # Determine the number of rows of aliens that fit the screen.
        ship_height = self.ship.rect.height
        available_space_y = (
            self.settings.screen_height - (3 * alien_height) - ship_height
        )

        number_rows = available_space_y // (2 * alien_height)

        # Create the full fleet of aliens.
        for row in range(number_rows):
            for alien_number in range(int(number_aliens_x)):
                self._create_alien(alien_number, row)

    def _create_alien(self, alien_number, row_number):
        """Create an aliena and place it in a row."""
        rand_num = randint(-60, 60)
        rand_num_2 = randint(-40, 40)
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + (2 * alien.rect.height * row_number)
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

        # self.aliens.add(alien)

    

    def display_time(self):
        self.time_used = self.clock.tick(30)
        if self.stats.game_active:
            self.start_time += self.time_used / 1000 #add time used to start time
        
        self.time_format = str(int(self.start_time * 10) / 10)
        self.time_display = self.myfont15.render(
            f"Time elapsed : {self.time_format} seconds", 1, (0, 0, 0)
        )
        #return self.display
        self.screen.blit(self.time_display, (20, 20))
  
        

    def instruct(self):
        self.label = self.myfont15.render(
            "Avoid The Aliens and Shoot to kill them", 1, (255, 0, 0)
        )
        self.screen.blit(self.label, (20, 650))

    def _update_bullets(self):
        """Updates the position of bullets and get rid of old bullets"""
        # Update bullets positions.
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        # Check for any bullets that have hit aliens.
        # If there is hit, get rid of the bullet and the alien.
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """Check for any bullets that have hit aliens.
        If there is hit, get rid of the bullet and the alien."""
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        # Repopulate the fleet
        if not self.aliens:
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                #Treat this the same as if the ship got hit.
                self._ship_hit()
                break

    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left > 0:
            #Decrease the ships left.
            self.stats.ships_left -= 1

            #Get rid of any remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            #Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()

            #Pause for 0.5 sec.
            sleep(0.5)
        else:
            self.stats.game_active = False
    def _update_aliens(self):
        """Update the positions of all aliens in the fleet."""
        self._check_fleet_edges()
        self.aliens.update()

        #Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        self._check_aliens_bottom()


    def _update_screen(self):
        """Update images on the screen, and flip to the new screeen.
        Everything to be displayed on the screen should be between the screen fill and display_flip methods."""

        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()  # makes ship appear on top of background

        self.instruct()
        self.display_time()
        
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == "__main__":
    # Make game intance and run the game.
    ai = AlienInvasion()
    ai.run_game()
