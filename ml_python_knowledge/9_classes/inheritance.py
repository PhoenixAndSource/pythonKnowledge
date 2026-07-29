## when a class (child class) inherits from another class (parent class).
# a child class can inherit all attributes and methods of parent class
# while allowed their own new attributes and methods.

## __init__() Method for Child Class
# call __init__() method from the parent class as your creating a new class from the parent.

# example: model an art piece. we'll write attributes and behaviours specific to art pieces.

class ArtPiece:
    """represent an art piece."""

    def __init__(self, medium, type_of_canvas, subject, amount_of_detail):
        """Initialize attributes to describe an art piece."""
        self.medium = medium
        self.type_of_canvas = type_of_canvas
        self.subject = subject
        self.amount_of_detail = amount_of_detail

    def get_description_art_piece(self):
        """Return a description of the art piece"""
        title_art = f"{self.medium} {self.type_of_canvas} {self.subject}"
        return title_art.title()

    def read_amount_of_detail(self):
        """Print a statement showing the amount of detail in art piece."""
        print(f"This art piece has {self.amount_of_detail} amount of detail in it.")

    def update_amount_of_detail(self, detail_amount):
        """Set the amount of detail to the given value."""
        if detail_amount >= self.detail_amount:
            self.amount_of_detail = detail_amount
        else:
            print("sometimes, one can't have less detail without a type of eraser.") 

class BeautifulArtPiece(ArtPiece):
    """Represent parts of an art piece, specific to a beautiful art piece."""

    def __init___(self, medium, type_of_canvas, subject, amount_of_detail):
        """Initialize attributes of parent class"""
        super().__init__(medium, type_of_canvas, subject, amount_of_detail)

my_beautiful_art_piece = BeautifulArtPiece('acrylic', 'linen washed evenly with gesso', 'the male gaze', 3)
print(my_beautiful_art_piece.get_description_art_piece())

## Define Attributes and Methods for Child Class
# add attribute specific to beautiful art pieces from the parent class art piece
# add method to report on above attribute.
# do this by storing canvas size and write a method that prints description of canvas size.
# you can add unlimited attributes and methods

class ArtPiece:
    """represent an art piece."""

    def __init__(self, medium, type_of_canvas, subject, amount_of_detail):
        """Initialize attributes to describe an art piece."""
        self.medium = medium
        self.type_of_canvas = type_of_canvas
        self.subject = subject
        self.amount_of_detail = 0

    def get_description_art_piece(self):
        """Return a description of the art piece"""
        title_art = f"{self.medium} {self.type_of_canvas} {self.subject}"
        return title_art.title()

    def read_amount_of_detail(self):
        """Print a statement showing the amount of detail in art piece."""
        print(f"This art piece has {self.amount_of_detail} amount of detail in it.")

    def update_amount_of_detail(self, detail_amount):
        """Set the amount of detail to the given value."""
        if detail_amount >= self.amount_of_detail:
            self.amount_of_detail = detail_amount
        else:
            print("sometimes, one can't have less detail without a type of eraser.") 

class BeautifulArtPiece(ArtPiece):
    """Represent parts of an art piece, specific to a beautiful art piece."""

    def __init__(self, medium, type_of_canvas, subject, amount_of_detail):
        """Initialize attributes of parent class
        Then initialize attributes specific to a beautiful painting.
        """
        super().__init__(medium, type_of_canvas, subject, amount_of_detail)
        self.canvas_size = 89

    def describe_canvas_size(self):
        """Print a statement describing canvas size."""
        print(f"This beautiful art piece has a canvas size of {self.canvas_size}!")

my_beautiful_art_piece = BeautifulArtPiece('acrylic', 'linen washed evenly with gesso', 'the male gaze', 3)
print(my_beautiful_art_piece.get_description_art_piece())
my_beautiful_art_piece.describe_canvas_size()

## Override Methods from Parent Class
# define a method in the child class with the same name of the method you wish to override.
# then Python will ignore the original parent class method!
# then Python will just use the newly defined child class method.


class ArtPiece:
    """represent an art piece."""

    def __init__(self, medium, type_of_canvas, subject, amount_of_detail):
        """Initialize attributes to describe an art piece."""
        self.medium = medium
        self.type_of_canvas = type_of_canvas
        self.subject = subject
        self.amount_of_detail = 0

    def get_description_art_piece(self):
        """Return a description of the art piece"""
        title_art = f"{self.medium} {self.type_of_canvas} {self.subject}"
        return title_art.title()

    def read_amount_of_detail(self):
        """Print a statement showing the amount of detail in art piece."""
        print(f"This art piece has {self.amount_of_detail} amount of detail in it.")

    def update_amount_of_detail(self, detail_amount):
        """Set the amount of detail to the given value."""
        if detail_amount >= self.amount_of_detail:
            self.amount_of_detail = detail_amount
        else:
            print("sometimes, one can't have less detail without a type of eraser.") 

    def use_linseed_oil(self):
        """Print a statement of the importance of washing your oil brushes with linseed oil after using them."""
        print("If using oil paint, wash brushes with linseed oil.")

class BeautifulArtPiece(ArtPiece):
    """Represent parts of an art piece, specific to a beautiful art piece."""

    def __init__(self, medium, type_of_canvas, subject, amount_of_detail):
        """Initialize attributes of parent class
        Then initialize attributes specific to a beautiful painting.
        """
        super().__init__(medium, type_of_canvas, subject, amount_of_detail)
        self.canvas_size = 89

    def describe_canvas_size(self):
        """Print a statement describing canvas size."""
        print(f"This beautiful art piece has a canvas size of {self.canvas_size}!")

    def use_linseed_oil(self):
        """beautiful art pieces using acrylic paint don't need linseed oil."""
        print("This painting does not use linseed oil.")

my_beautiful_art_piece = BeautifulArtPiece('acrylic', 'linen washed evenly with gesso', 'the male gaze', 3)
print(my_beautiful_art_piece.get_description_art_piece())
my_beautiful_art_piece.describe_canvas_size()
my_beautiful_art_piece.use_linseed_oil()


## Instances as Attributes
# when you have a lot of attributes and methods,
# you can reduce your files 
# by writing a part of a class as a separate class.
# break large class into smaller classes that work as a team
# this is called COMPOSITION.

# example: use MagicProtectionSymbols as an instance as an attribute in BeautifulArtPiece class.

class ArtPiece:
    """represent an art piece."""

    def __init__(self, medium, type_of_canvas, subject, amount_of_detail):
        """Initialize attributes to describe an art piece."""
        self.medium = medium
        self.type_of_canvas = type_of_canvas
        self.subject = subject
        self.amount_of_detail = 0

    def get_description_art_piece(self):
        """Return a description of the art piece"""
        title_art = f"{self.medium} {self.type_of_canvas} {self.subject}"
        return title_art.title()

    def read_amount_of_detail(self):
        """Print a statement showing the amount of detail in art piece."""
        print(f"This art piece has {self.amount_of_detail} amount of detail in it.")

    def update_amount_of_detail(self, detail_amount):
        """Set the amount of detail to the given value."""
        if detail_amount >= self.amount_of_detail:
            self.amount_of_detail = detail_amount
        else:
            print("sometimes, one can't have less detail without a type of eraser.") 

    def use_linseed_oil(self):
        """Print a statement of the importance of washing your oil brushes with linseed oil after using them."""
        print("If using oil paint, wash brushes with linseed oil.")

class MagicProtectionSymbols:
    """model magic protection symbols for an art piece."""

    def __init__(self, magic_protection_symbols_amount=1):
        """Initialize the magic protection symbols attributes."""
        self.magic_protection_symbols_amount = magic_protection_symbols_amount

    def describe_magic_protection_symbols(self):
        """Print a statement describing the magic protection symbols amount."""
        print(f"This art piece has a {self.magic_protection_symbols_amount}.")

class BeautifulArtPiece(ArtPiece):
    """Represent parts of an art piece, specific to a beautiful art piece."""

    def __init__(self, medium, type_of_canvas, subject, amount_of_detail):
        """Initialize attributes of parent class
        Then initialize attributes specific to a beautiful painting.
        """
        super().__init__(medium, type_of_canvas, subject, amount_of_detail)
        self.canvas_size = 89

    def describe_canvas_size(self):
        """Print a statement describing canvas size."""
        print(f"This beautiful art piece has a canvas size of {self.canvas_size}!")

    def use_linseed_oil(self):
        """beautiful art pieces using acrylic paint don't need linseed oil."""
        print("This painting does not use linseed oil.")

my_beautiful_art_piece = BeautifulArtPiece('acrylic', 'linen washed evenly with gesso', 'the male gaze', 3)
print(my_beautiful_art_piece.get_description_art_piece())
my_beautiful_art_piece.describe_canvas_size()
my_beautiful_art_piece.use_linseed_oil()
my_beautiful_art_piece.magic_protection_symbols.describe_magic_protection_symbols()
my_beautiful_art_piece.magic_protection_symbols.get_layers_of_magic()

# add another method that reports layers of magic based on MagicProtectionSymbols.

class ArtPiece:
    """represent an art piece."""

    def __init__(self, medium, type_of_canvas, subject, amount_of_detail):
        """Initialize attributes to describe an art piece."""
        self.medium = medium
        self.type_of_canvas = type_of_canvas
        self.subject = subject
        self.amount_of_detail = amount_of_detail

    def get_description_art_piece(self):
        """Return a description of the art piece"""
        title_art = f"{self.medium} {self.type_of_canvas} {self.subject}"
        return title_art.title()

    def read_amount_of_detail(self):
        """Print a statement showing the amount of detail in art piece."""
        print(f"This art piece has {self.amount_of_detail} amount of detail in it.")

    def update_amount_of_detail(self, detail_amount):
        """Set the amount of detail to the given value."""
        if detail_amount >= self.amount_of_detail:
            self.amount_of_detail = detail_amount
        else:
            print("sometimes, one can't have less detail without a type of eraser.") 

    def use_linseed_oil(self):
        """Print a statement of the importance of washing your oil brushes with linseed oil after using them."""
        print("If using oil paint, wash brushes with linseed oil.")

class MagicProtectionSymbols:
    """model magic protection symbols for an art piece."""

    def __init__(self, magic_protection_symbols_amount=1):
        """Initialize the magic protection symbols attributes."""
        self.magic_protection_symbols_amount = magic_protection_symbols_amount

    def describe_magic_protection_symbols(self):
        """Print a statement describing the magic protection symbols amount."""
        print(f"This art piece has a {self.magic_protection_symbols_amount}.")

    def get_layers_of_magic(self):
        """Print a statement about the layers of magic this magic protection symbol provides."""
        layers_of_magic = 1 # default value
        if self.magic_protection_symbols_amount == 33:
            layers_of_magic = 2
        elif self.magic_protection_symbols_amount == 66:
            layers_of_magic = 88

        print(f"This Magic Protection Symbol has about {layers_of_magic} layers of magic as it is.")

class BeautifulArtPiece(ArtPiece):
    """Represent parts of an art piece, specific to a beautiful art piece."""

    def __init__(self, medium, type_of_canvas, subject, amount_of_detail, magic_symbols_amount=1):
        """Initialize attributes of parent class
        Then initialize attributes specific to a beautiful painting.
        """
        super().__init__(medium, type_of_canvas, subject, amount_of_detail)
        self.canvas_size = 89
        self.magic_protection_symbols = MagicProtectionSymbols(magic_symbols_amount)

    def describe_canvas_size(self):
        """Print a statement describing canvas size."""
        print(f"This beautiful art piece has a canvas size of {self.canvas_size}!")

    def use_linseed_oil(self):
        """beautiful art pieces using acrylic paint don't need linseed oil."""
        print("This painting does not use linseed oil.")

my_beautiful_art_piece = BeautifulArtPiece('acrylic', 'linen washed evenly with gesso', 'the male gaze', 3, 33)
print(my_beautiful_art_piece.get_description_art_piece())
my_beautiful_art_piece.describe_canvas_size()
my_beautiful_art_piece.use_linseed_oil()
my_beautiful_art_piece.magic_protection_symbols.get_layers_of_magic()
