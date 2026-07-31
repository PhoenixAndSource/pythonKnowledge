import pygame
from pygame.sprite import Sprite

class LoveBird(Sprite):
    """A class to represent a single lovebird in the fleet."""

    def __init__(self, ai_game):
        """Initialize the lovebird and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the lovebird image and set its rect attribute.
        self.image = pygame.image.load('images/lovebird.bmp')
        self.rect = self.image.get_rect()

        # Start each new lovebird near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the lovebird's exact horizontal position.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if lovebird is at the edge of the screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        """Fly the lovebird to the right."""
        self.x += self.settings.lovebird_speed * self.settings.flock_direction
        self.rect.x = self.x