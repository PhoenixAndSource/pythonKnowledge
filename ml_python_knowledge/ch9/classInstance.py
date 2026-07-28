# modify attributes connected with instance.
# modify directly, or write methods that update attributes

class Bunny:
    """represent a bunny"""

    def __init__(self, fur, noise, growth):
        """Initialize attributes to describe a bunny."""
        self.fur = fur 
        self.noise = noise
        self.growth = growth

    def get_bunny_name(self):
        """Return a formatted bunny name."""
        total_name = f"{self.fur} {self.noise} {self.growth}"
        return total_name.title()

my_cute_bunny = Bunny('fluffy', 'sniff', 'wise baby')
print(my_cute_bunny.get_bunny_name())

## Set default value for attribute
# instance creation still allows attributes to be defined without being pass as parameters.
# the attributes are assigned a default value via the __init__() method

# Let's bring in an attribute called bunny_growth that starts with a value of 0.
# Let's bring in a method called read_bunny_growth() that helps us see how many hours of meditation the bunny has reached so far.

class Bunny:

    def __init__(self, fur, noise, growth):
        """Initialize attributes to describe bunny."""
        self.fur = fur
        self.noise = noise
        self.growth = growth
        self.bunny_growth = 0

    def get_bunny_name(self):
        """Return a formatted bunny name."""
        total_name = f"{self.fur} {self.noise} {self.growth}"
        return total_name.title()

    def read_bunny_growth(self):
        """Print how many hours of meditation bunny has dedicated so far."""
        print(
            f"This bunny's day has been fruitful, as bunny has dedicated {self.bunny_growth} meditation hours today."
            )

my_cute_bunny = Bunny('soft', 'purrr', 'wise baby')
print(my_cute_bunny.get_bunny_name())
my_cute_bunny.read_bunny_growth()

## Modify an Attribute's Value Via Method
# pass the new value to a method, instead of accessing attribute directly.
# example: update_bunny_growth()

class Bunny:

    def __init__(self, fur, noise, growth):
        """Initialize attributes to describe bunny."""
        self.fur = fur
        self.noise = noise
        self.growth = growth
        self.bunny_growth = 0

    def get_bunny_name(self):
        """Return a formatted bunny name."""
        total_name = f"{self.fur} {self.noise} {self.growth}"
        return total_name.title()

    def read_bunny_growth(self):
        """Print how many hours of meditation bunny has dedicated so far."""
        print(
            f"This bunny's day has been fruitful, as bunny has dedicated {self.bunny_growth} meditation hours today."
        )

    def update_bunny_growth(self, meditation_hours):
        """
        Set the meditation hours to the given value.
        Reject the change if the hours lower.
        """
        if meditation_hours >= self.bunny_growth:
            self.bunny_growth = meditation_hours
        else:
            print("Hours spent in meditation do not decrease")

## Incrementing Attribute's Value via a Method
# Increment attribute's value instead of assigning a new value.
# example add incremental amount to read bunny growth.

class Bunny:

    def __init__(self, fur, noise, growth):
        """Initialize attributes to describe bunny."""
        self.fur = fur
        self.noise = noise
        self.growth = growth
        self.bunny_growth = 0

    def get_bunny_name(self):
        """Return a formatted bunny name."""
        total_name = f"{self.fur} {self.noise} {self.growth}"
        return total_name.title()

    def read_bunny_growth(self):
        """Print how many hours of meditation bunny has dedicated so far."""
        print(
            f"This bunny's day has been fruitful, as bunny has dedicated {self.bunny_growth} meditation hours today."
        )

    def update_bunny_growth(self, meditation_hours):
        """
        Set the meditation hours to the given value.
        Reject the change if the hours lower.
        """
        if meditation_hours >= self.bunny_growth:
            self.bunny_growth = meditation_hours
        else:
            print("Hours spent in meditation do not decrease")

    def increment_meditation_hours(self, meditation_hours):
        """Add given amount to meditation hour reading."""
        self.bunny_growth += meditation_hours

my_brave_bunny = Bunny('soft', 'prettypurrr', 'brave and wise')
print(my_brave_bunny.get_bunny_name())

my_brave_bunny.update_bunny_growth(3)
my_brave_bunny.read_bunny_growth()

my_brave_bunny.increment_meditation_hours(2)
my_brave_bunny.read_bunny_growth()

# another choice is to modify the method to reject negative increments.