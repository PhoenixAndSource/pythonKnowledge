class Settings:
    """A class to store all settings for Cupid's Arrow."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (75, 0, 130)

        # Phoenix settings
        self.phoenix_speed = 1.5 # (moves by 1.5 pixels)
        self.phoenix_limit = 3

        # Arrow settings
        self.arrow_speed = 2.5
        self.arrow_width = 3
        self.arrow_height = 15
        self.arrow_color = (80, 80, 80)
        self.arrows_allowed = 3
        # arrows should be faster than the Phoenix.

        # LoveBird settings
        self.alien_speed = 1.0
        self.flock_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        # How quickly the lovebird point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

        # flock_direction of 1 represents right; -1 represents left.
        self.flock_direction = 1

    def initialize_dynamic_settings(self):
        self.phoenix_speed = 1.5
        self.arrow_speed = 2.5
        self.lovebird_speed = 1.0

        # flock_direction of 1 represents right; -1 represents left.
        self.flock_direction = 1

        # Scoring settings
        self.lovebird_points = 50

    def increase_speed(self):
        """Increase speed settings and lovebird point values."""
        self.phoenix_speed *= self.speedup_scale
        self.arrow_speed *= self.speedup_scale
        self.lovebird_speed *= self.speedup_scale

        self.lovebird_points = int(self.lovebird_points * self.score_scale)
        print(self.lovebird_points)




