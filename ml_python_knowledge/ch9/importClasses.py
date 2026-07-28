# keep organized: Python allows you store classes in modules 
# and then import the classes you need into your main program

## import a single class
# house.py

class House:
    """represent a house."""

    def __init__(self, land, architecture, view):
        """Initialize attributes to describe a house."""
        self.land = land
        self.architecture = architecture
        self.view = view
        self.read_money_available = 0

    def get_descriptive_name(self):
        """Return a descriptive name."""
        complete_name = f"{self.view} {self.land} {self.architecture}"
        return complete_name.title()

    def display_money_available(self):
        """Print a statement showing the money available for house."""
        print(f"I have this amount of money available: {self.read_money_available}.")

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

    def __init__(self, fertile_land, luxury_modern, mountains_water_and_beautiful_sunset_skies)
        """
        Initialize attributes of the parent class.
        then initialize attributes specific to a dream house.
        """
        super().__init__(land, architecture, view)
        self.adu = ADU()

# my_house.py

from house import House

my_dream_house = House('luscious', 'tall & modern', 'water & mountains')
print(my_dream_house.get_descriptive_name())
my_dream_house.read_available_to_buy = 91000000
my_dream_house.display_money_available()

# the import statement tells Python 
# to open the house module and import the class House.


## Store Multiple Classes in a Module
# let's add Accessory Dwelling Unit and Garage to module house.py

## Import an Entire Module
# using dot notation.
# every creation of an instance includes the module name
# hence no naming conflicts.

## Import All Classes from a Module

# the following example is not recommended
from module_example import *

# instead we want import statements at the top of a file.
# to see which classes are being used in the program clearly.

# best way to import a lot of classes from a module is
# importing the entire module
# module_example.ClassExample

## import a module into a module
# example: store House class in one module, and DreamHouse and ADU in a different module.
# let's make a new module called dream_house.py

## Alias examples:

from dream_house import DreamHouse as DH

my_dream_house = DH('river', 'modern architectural gem', 'beach')

# another alias example

import dream_house as dh

my_dream_house = dh.DreamHouse('beach', 'beautiful home', 'beach and mountains')
