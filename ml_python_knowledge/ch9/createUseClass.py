## Object-oriented programming (OOP)
# Instantiation: making an object from a class
# you work with instances of a class.
# let's write classes and create instances of those classes
# info can be stored in instances
# we can write actions for the instances.
# classes can create and allow more functionality of existing classes
# similar classes can share common functionality.
# store classes in modules
# import classes into program files.

# let's make a class named water bottle
# it will store a shape and drink, the ability to hold_hot_drinks() and hold_cold_drinks():

# classes are usually capitalized by convention.

class WaterBottle:
    """Simple model of a water bottle."""

    def __init__(self, shape, drink):
        """Initialize shape and drink attributes."""
        self.shape = shape
        self.drink = drink

    def hold_hot_drinks(self):
        """Simulate a water bottle holding a hot drink."""
        print(f"{self.shape} is not holding a hot drink.")

    def hold_cold_drinks(self):
        """Simulate holding cold drinks"""
        print(f"{self.shape} is holding a cold drink.")

## The __init__() Method
# a Method is a function that's part of a class.
#__init__() is a special method, automatically run each time a new instance is created based on the WaterBottle class.

# it has two underscores before and after init. this convention helps it from conflicting with your method names.
# it requires two underscores before and after otherwise the method won't be called automatically which will result in an errors.

# the self parameter: required in method definition. It needs to always be the first parameter.

# attributes are variables via instances

## Creating an Instance from a Class
# a class is basically instructions to create an instance.
# the WaterBottle class is a set of instructions on how to make instances that are specific water bottle types.

class WaterBottle:
    """Simple model of a water bottle."""

    def __init__(self, shape, drink):
        """Initialize shape and drink attributes."""
        self.shape = shape
        self.drink = drink

    def hold_hot_drinks(self):
        """Simulate a water bottle holding a hot drink."""
        print(f"{self.shape} is not holding a hot drink.")

    def hold_cold_drinks(self):
        """Simulate holding cold drinks"""
        print(f"{self.shape} is holding a cold drink.")

my_water_bottle = WaterBottle('mug', 'matcha tea')

print(f"My water bottle is in the shape of a {my_water_bottle.shape}.")
print(f"My water bottle is filled with {my_water_bottle.drink}.")

## Access Attributes
# use dot notation:
my_water_bottle.shape

## Creating Multiple Instances
# Create a second water bottle called future_water_bottle:

class WaterBottle:
    """Simple model of a water bottle."""

    def __init__(self, shape, drink):
        """Initialize shape and drink attributes."""
        self.shape = shape
        self.drink = drink

    def hold_hot_drinks(self):
        """Simulate a water bottle holding a hot drink."""
        print(f"{self.shape} is not holding a hot drink.")

    def hold_cold_drinks(self):
        """Simulate holding cold drinks"""
        print(f"{self.shape} is holding a cold drink.")

my_water_bottle = WaterBottle('mug', 'matcha tea')
my_future_water_bottle = WaterBottle('borosilicate glass and bamboo or silver bottle', 'matcha soy milk latte')

print(f"My beautiful and clean water bottle is a {my_water_bottle.shape}.")
print(f"My beautiful, and clean water bottle is filled with amazing {my_water_bottle.drink}")
my_water_bottle.hold_hot_drinks()

print(f"\nMy clean and beautiful future water bottle is {my_future_water_bottle.shape} and better!")
print(f"My clean and beautiful future water bottle is filled with amazing {my_future_water_bottle.drink}")
my_water_bottle.hold_hot_drinks()