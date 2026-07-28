"""A set of classes that can be used to represent dream houses."""

from house import House

class ADU:
    """
    model an Accessory Dwelling Unit for my dream house.
    """

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

# class DreamHouse needs to able to connect to its parent class House,
# so that's why we import House directly into module.
class DreamHouse(House):
    """Aspects of houses, specific to dream houses."""

    def __init__(self, land, architecture, view):
        """
        Initialize attributes of the parent class.
        then initialize attributes specific to a dream house.
        """
        super().__init__(land, architecture, view)
        self.adu = ADU()