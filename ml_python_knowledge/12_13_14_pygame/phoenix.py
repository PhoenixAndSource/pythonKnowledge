# Pygame allows you to treat all game elements as rectangles (rects),
# even if they're not shaped like rectangles.

import pygame
from pygame.sprite import Sprite

class Phoenix(Sprite):
    """A class to manage the Phoenix."""

    def __init__(self, ai_game): # this method uses two parameters, self and current instance of CupidsArrow class, which allows access to all game resources in CupidsArrow.
        """Initialize the Phoenix and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen # assign screen to attribute of Phoenix,  to access in all methods in this class.
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect() # this helps us place Phoenix in the correct position.

        # Load the Phoenix image and get its rect.
        self.image = pygame.image.load('images/phoenix.bmp')
        self.rect = self.image.get_rect()

        # Start each new Phoenix at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a float for the Phoenix's exact horizontal position.
        self.x = float(self.rect.x)

        # Flying flag; with with a Phoenix that is in sitting meditation.
        self.flying_right = False
        self.flying_left = False

    def update(self):
        """Update Phoenix's position based on flying flag."""
        # Refresh the Phoenix's x value, not the rect.
        if self.flying_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.phoenix_speed
        if self.flying_left and self.rect.left > 0:
            self.x -= self.settings.phoenix_speed

        # Update rect object from self.x.
        self.rect.x = self.x

    def blitme(self):
        """Draw the Phoenix at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_phoenix(self):
        """Center the phoenix on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

        