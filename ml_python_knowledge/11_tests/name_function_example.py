# a function that grabs your first and last name and outputs the user's complete name with appropriate capitalization.

def get_complete_name(first, last):
    """Create the user's complete name."""
    complete_name = f"{first} {last}"
    return complete_name.title()

## middle name argument:
# example of failing test:

def get_complete_name(first, middle, last):
    """Create a capitalized full name."""
    complete_name = f"{first} {middle} {last}"
    return complete_name.title()

# on the output of failed test, > angle bracket shows line of code that made test fail.
# E shows exact error that made it fail.
# summary of reason for failure at the end.

# let's make the middle name optional and run the test. 

def get_complete_name(first, last, middle=''): # move middle to the end, and give it an empty value.
    """Create a capitalized, ordered complete name."""
    if middle:
        complete_name = f"{first} {middle} {last}"
    else:
        complete_name = f"{first} {last}"
    return complete_name.title()

# now the test passes.
