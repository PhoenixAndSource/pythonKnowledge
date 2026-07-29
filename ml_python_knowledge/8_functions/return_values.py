## return statement grabs a value from inside a function, 
# and delivers it back to the code that called the function.

# function grabs first name and last name, and spits out a full name.
# get_formatted_name function is an example that is 
# useful if you have a lot of first names and last names stored separately.

def get_formatted_name(first_name, last_name):
    """Spit out your full name, formatted correctly."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

goddess = get_formatted_name('phoenix', 'star')
print(goddess)

## turn argument optional.
def grab_complete_name(first_name, middle_name, last_name):
    """Grab a complete name."""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

goddess = grab_complete_name('phoenix', 'star', 'god')
print(goddess)

# make the middle name optional
# middle_name's value is an empty string
# first and last name parameters are first.
#python reads non-empty strings as True.
# if there is no middle name, then the empty string does not pass the if test, so the else block is activated.

def grab_complete_name(first_name, last_name, middle_name=''):
    """Spell out complete name, in order."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

goddess = grab_complete_name('phoenix', 'star')
print(goddess)

goddess = grab_complete_name('berry', 'ice', 'lemonade')
print(goddess)

## Returning a Dictionary
# functions will return any value, ie: lists and dictionaries

# character_info grabs a first name and last name
# then puts these names into a dictionary

def character_info(first_name, last_name):
    """Return a dictionary with information about a character."""
    character = {'first': first_name, 'last': last_name} # 'first' is the key, and first_name is the value.
    return character

goddess = character_info('phoenix', 'star')
print(goddess)

# store optional values such as age.
# optional parameter is age, and give it the special value of None. 
# None is used when there is not specific value assigned to it.
# None is read as False in a conditional test.
def character_info(first_name, last_name, age=None):
    """Return a dictionary with info about a character"""
    character = {'first': first_name, 'last': last_name}
    if age:
        character['age'] = age
    return character

goddess = character_info('phoenix', 'star', age=27)
print(goddess)


## Function with while Loop
# say hello with first and last names:

def grab_complete_name(first_name, last_name):
    """Return a full name, in order."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# here is an infinite loop
#while True:
    print("\nWhat's your name?")
    f_name = input("First name: ")
    l_name = input("Last name: ")

    complete_name = grab_complete_name(f_name, l_name)
    print(f"\nHello, {complete_name}!")

# offer a way to quit the program at each prompt:
def grab_complete_name(first_name, last_name):
    """Return a complete name, ordered"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nWhat is your name?")
    print("(type 'q' anytime to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    complete_name = grab_complete_name(f_name, l_name)
    print(f"\nHi, {complete_name}!")
