import pygame
from pygame.sprite import Sprite

class Arrow(Sprite): # sprites can help you group related elements in game and work on all grouped elements at once.
    """A class to manage arrows fired from Phoenix."""

    def __init__(self, ai_game):
        # __init__() needs current instance of CupidsArrows
        """Create an arrow object at the Phoenix's current position."""
        super().__init__() # super() helps inherit from Sprite.
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.arrow_color

        # Create an arrow rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.arrow_width,
            self.settings.arrow_height)
        self.rect.midtop = ai_game.phoenix.rect.midtop

        # Store the arrow's position as a float.
        self.y = float(self.rect.y)

    def update(self):
        """Shoot arrow up the screen."""
        # Refresh the exact position of the arrow.
        self.y -= self.settings.arrow_speed
        # Refresh the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the arrow to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)