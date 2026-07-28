class House:
    """represent a house."""

    def __init__(self, land, architecture, view):
        """Initialize attributes to describe a house."""
        self.land = land
        self.architecture = architecture
        self.view = view
        self.read_money_available = 100000000

    def get_descriptive_name(self):
        """Return a descriptive name."""
        complete_name = f"{self.view} {self.land} {self.architecture}"
        return complete_name.title()

    def display_money_available(self):
        """Print a statement showing the money of the highest currency available for house."""
        print(f"I have this amount of money of the highest currency available: {self.read_money_available}.")

    def update_money_available(self, money_amount):
        """
        Set the amount of money available to the given value.
        Reject the change if amount lessens.
        """
        if money_amount >= self.read_money_available:
            self.read_money_available = money_amount
        else:
            print("you can't have less money available for yourself!")

    def increment_money_available(self, money):
        """Add the given amount to the money available."""
        self.read_money_available += money