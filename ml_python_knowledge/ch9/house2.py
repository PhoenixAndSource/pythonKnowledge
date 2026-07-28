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

class ADU:
    """model an Accessory Dwelling Unit for my dream house."""

    def __init__(self, adu_sqft=4000):
        """Initialize the accessory dwelling unit's attributes."""
        self.adu_sqft = adu_sqft

    def describe_adu(self):
        """Print a statement describing the size of ADU."""
        print(f"This ADU has {self.adu_sqft} square feet.")

    def get_what_adu_does(self):
        """Print a statement about what the adu does"""
        if self.adu_sqft == 3000:
            highest_currency_income_per_month = 30000
        elif self.adu_sqft == 5000:
            highest_currency_income_per_month = 90000

        print(f"This ADU can make at least {highest_currency_income_per_month} of currency of the highest worth.")

class DreamHouse(House):
    """Aspects of houses, specific to dream houses."""

    def __init__(self, land, architecture, view):
        """
        Initialize attributes of the parent class.
        then initialize attributes specific to a dream house.
        """
        super().__init__(land, architecture, view)
        self.adu = ADU()