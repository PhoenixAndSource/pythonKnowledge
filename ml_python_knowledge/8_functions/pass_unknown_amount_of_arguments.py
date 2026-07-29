# the function here, works with one value or more values.
# asterisk in parameter name *magic_items (splat operator or unpacking operator) 
# asks python to create a tuple called magic_items 
# so that you don't have to write separate functions for each argument.
def create_magic(*magic_items):
    """Print the list of magic ingredients that the spell asks for"""
    print(magic_items)

create_magic('potassium')
create_magic('laptop', 'consistency', 'belief', 'self-perseverance')

#replace print() call with loop that loops through magic_items and tells us about the creation of magic.
def create_magic(*magic_items):
    """tell us about the magic we are creating"""
    print("\nCreating magic with these ingredients:")
    for magic_item in magic_items:
        print(f"- {magic_item}")

create_magic('banana', 'laptop', 'self-perseverence', 'self-belief', 'appropriate actions', 'coffee/matcha/drink', 'phone', 'textbook')

## Mix Positional and Arbitrary Arguments
# you can mix positional, keyword, and arbitrary values
# How to write function to work with arbitrary number of arguments:
# in function definition, put parameter that works with arbitrary number of arguments, last.

def create_magic(numberBreaths, *magic_items):
    """Tell us about the magic we are going to create."""
    print(f"\nCreating magic in {numberBreaths} breaths:")
    for magic_items in magic_items:
        print(f"- {magic_items}")

create_magic(3, 'laptop')
create_magic(2, 'yoga', 'self-confidence', 'breeze')

## Using Arbitrary Keyword Arguments
# for unknown info that will be passed to function.
# example, user profiles

def create_character(first, last, **character_info):
    """Make a dictionary that has all info known about character."""
    character_info['first_name'] = first
    character_info['last_name'] = last
    return character_info

character_profile = create_character('goddess', 'phoenix',
                                     location='heaven',
                                     specialty='flying')
print(character_profile)

# create_character gives user unlimited name-value pairs.
# ** double asterisks with parameter character_info makes Python create a dictionary called character_info
