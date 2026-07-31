## How to create an empty Pygame window:
# make a class to represent the game.

import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import ScoreBoard
from button import Button
from phoenix import Phoenix
from arrow import Arrow
from lovebird import LoveBird

class CupidsArrow:
    """CEO of classes to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, make game resources."""
        pygame.init()

        self.clock = pygame.time.Clock() 
        # this helps the game run consistently at the same speed or frame rate across all systems
        # class Clock is from the pygame.time module.

        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)) # A surface in this case is the object assigned to self.screen
        pygame.display.set_caption("Cupid's Arrow") # surface returned by display.set_mode() which is the entire screen window.

        # Create an instance to store game statistics,
        #   and create a scoreboard.
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.phoenix = Phoenix(self)
        self.arrows = pygame.sprite.Group()
        self.lovebirds = pygame.sprite.Group()

        # Start Cupid's Arrow in an active state.
        self.game_active = True

        # Start Cupid's Arrow in an inactive state.
        self.game_active = False

    def _create_flock(self):
        """Create the flock of lovebirds."""
        # Create a lovebird and keep adding lovebirds until the space is filled.
        # Spacing between lovebirds is a lovebird width and one lovebird height.
        lovebird = LoveBirds(self)
        lovebird_width, lovebird_height = lovebird.rect.size

        current_x, current_y = lovebird_width, lovebird_height
        while current_y < (self.settings.screen_height - 3 * lovebird_height):
            while current_x < (self.settings.screen_width - 2 * lovebird_width):
                self._create_lovebird(current_x, current_y)
                current_x += 2 * lovebird_width

            # Finished a row; reset x value, and increment y value.
            current_x = lovebird_width
            current_y += 2 * lovebird_height

        # background color, otherwise the screen's default is black:
        self.bg_color = (75, 0, 130) # colors in Pygame are in RGB
        while current_x < (self.settings.screen_width - 2 * lovebird_width):
            self._create_lovebird(current_x)
            current_x += 2 * lovebird_width

    def _create_lovebird(self, x_position, y_position):
        """Create a lovebird and place it in the flock."""
        new_lovebird = LoveBird(self)
        new_lovebird.x = x_position
        new_lovebird.rect.x = x_position
        new_lovebird.rect.y = y_position
        self.lovebirds.add(new_lovebird)

    def _check_flock_edges(self):
        """Respond appropriately if any lovebirds have reached an edge."""
        for lovebird in self.lovebirds.sprites():
            if lovebird.check_edges():
                self._change_flock_direction()
                break

    def _change_flock_direction(self):
        """Drop the entire flock and change flock's direction."""
        for lovebird in self.lovebirds.sprites():
            lovebird.rect.y += self.settings.flock_drop_speed
        self.settings.flock_direction *= -1
        
    def run_game(self):
        """Start main loop for Cupid's Arrow."""
        while True:
            self._check_events()

            if self.game_active:
                self.phoenix.update()
                self._update_arrows()
                self._update_lovebirds()

            self._update_screen()

            self.clock.tick(50) 
            # make clock tick
            # tick method's argument: frame rate of game, which is 50 here.
            
            self.arrows.update()

            # Get rid of arrows that have disappeared.
            for arrow in self.arrows.copy():
                if arrow.rect.bottom <= 0:
                    self.arrows.remove(arrow)
            print(len(self.arrows))

            # redraw screen each loop pass:
            # fill screen with bg color with fill() method
            self.screen.fill(self.settings.bg_color)
            self.phoenix.blitme()
            
    def _check_events(self): # sees if player clicked to close window
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get.pos()
                self._check_play_button(mouse_pos)
            
            # elif event.type == pygame.KEYDOWN:
            #    self._check_keydown_events(event)
            # elif event.type == pygame.KEYUP:
            #    self._check_keyup_events(event)

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoints(mouse_pos)
        if button_clicked and not self.game_active:
            # Rest the game settings.
            self.settings.initialize_dynamic_settings()

            # Reset the game statistics.
            self.stats.reset_stats()
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_phoenixes()

            # Hide the mouse cursor,
            pygame.mouse.set_visible(False)

        if self.play_button.rect.collidepoint(mouse_pos):
            # Reset the game statistics.
            self.stats.reset_stats()
            self.game_active = True
            # Get rid of any remaining arrows and lovebirds.
            self.arrows.empty()
            self.lovebirds.empty()

            # Create a new flock and center the Phoenix.
            self._create_flock()
            self.phoenix.center_phoenix()

    def _check_keydown_events(self, event):
        """Respond to keypresses.""" 
        if event.key == pygame.K_RIGHT:
            # Phoenix flies to the right.
            self.phoenix.flying_right = True
        elif event.key == pygame.K_LEFT:
            self.phoenix.flying_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_arrows()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.phoenix.flying_right = False
        elif event.key == pygame.K_LEFT:
            self.phoenix.flying_left = False

            self.phoenix.rect.x += 1

    def _fire_arrows(self):
        """Create a new arrow and add it to the arrows group."""
        if len(self.arrows) < self.settings.arrows_allowed:
            new_arrow = Arrow(self)
            self.arrows.add(new_arrow)

    def _update_arrows(self):
        """Update position of arrows and get rid of old arrows."""
        # Update arrow positions.
        self.arrows.update()

        # Get rid of arrows that have disappeared.
        for arrow in self.arrows.copy():
            if arrow.rect.bottom <= 0:
                self.arrows.remove(arrow)

            self._check_arrow__lovebird_collisions()

    def _check_arrow_lovebird_collisions(self):
            """Respond to arrow-lovebird collisions."""
            # Remove any arrows and lovebirds that have collided.
            collisions = pygame.sprite.groupecollide(
                self.arrows, self.lovebirds, True, True)

        if collisions:
            for lovebirds in collisions.values():
                self.stats.score += self.settings.lovebird_points * len(lovebirds)
                self.stats.score += self.settings.lovebird_points
                self.sb.prep_score()
                self.sb.check_high_score()

        if not self.lovebirds:
            # Destroy existing arrows and create new flock.
            self.arrows.empty()
            self._create_flock()
            self.settings.increase_speed()

            # Increase level.
            self.stats.level += 1
            self.sb.prep_level()

    def _update_lovebirds(self):
        """Check if the flock is at the edge, then update positions."""
        self._check_flock_edges()
        self.lovebirds.update()

        # Look for lovebird-phoenix collisions.
        if pygame.sprite.spritecollideany(self.phoenix, self.lovebirds):
            self._phoenix_hit()
            print("Phoenix opens her heart!!!")

        # Looks for lovebirds hitting the bottom of the screen.
        self._check_lovebirds_bottom()

    def _update_screen(self):
        """Refresh images on screen, then flip to new screen."""
        self.screen.fill(self.settings.bg_color)
        for arrow in self.arrows.sprites():
            arrow.draw_arrow()
        self.phoenix.blitme()
        self.lovebirds.draw(self.screen)

        # Draw the score information.
        self.sb.show_score()

        # Draw the play button if the game is inactive.
        if not self.game_active:
            self.play_button.draw_button()

        # Reveal most recent drawn screen view.
        pygame.display.flip()

    def _create_flock(self):
        """Create the flock of lovebirds."""
        # Create a lovebird and continue creating lovebirds until they take up all the space.
        # Spacing between lovebirds is one lovebird's width.
        lovebird = LoveBird(self)
        lovebird_width = lovebird.rect.width

        current_x = lovebird_width
        while current_x < (self.settings.screen_width - 2 * lovebird_width):
            new_lovebird = LoveBird(self)
            new_lovebird.x = current_x
            new_lovebird.rect.x = current_x
            self.lovebirds.add(new_lovebird)
            current_x += 2 * lovebird_width
        self.lovebirds.add(lovebird)

    def _phoenix_hit(self):
        """Respond to the Phoenix being hit by an lovebird."""
        if self.stats.phoenixes_left > 0:
            # Decrement Phoenixes_left, and update scoreboard.
            self.stats.phoenixes_left -= 1
            self.sb.prep_phoenixes()

            # Get rid of any remaining arrows and lovebirds.
            self.arrows.empty()
            self.lovebirds.empty()

            # Create a new flock and center the Phoenix.
            self._create_flock()
            self.phoenix.center_phoenix()
            # Pause
            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

            # Make the PLay button.
            self.play_button = Button(self, "Play")

    def _check_lovebirds_bottom(self):
        """Check if any lovebirds have reached the bottom of the screen."""
        for lovebird in self.lovebirds.sprites():

            if lovebird.rect.bottom >= self.settings.screen_height:
                # Treat this the same as if the phoenix got hit.
                self.phoenix_hit()

if __name__ == '__main__':
    # Create a game instance, and start the game.
    ai = CupidsArrow()
    ai.run_game()

