from pathlib import Path
import json

name = input("Create your name: ") # prompt

path = Path('name.json') # write data to name.json
info = json.dumps(name)
path.write_text(info)

print(f"We've saved your name for the future, {name}! ")

## combine files
# retrieve name from memory, 
# or prompt for name, and store name in name.json

# instead of try-except block to respond 
# to potentially non-existant name.json file
# use exists() method from pathlib module!

from pathlib import Path
import json

path = Path('name.json')
if path.exists():
    info = path.read_text()
    name = json.loads(info)
    print(f"Hi {name} again!")
else:
    name = input("Your name again? ")
    info = json.dumps(name)
    path.write_text(info)
    print(f"Your name is saved, {name}!")


## Refactoring
# improve code by dividing it up into a series of functions 
# with its own jobs.

# this function say_hello() 
# 1. is getting a stored name if it exists
# 2. and prompting a name if it doesn't exist.

from pathlib import Path
import json

def say_hello():
    """Say hello to the user with their name."""
    path = Path('name.json')
    if path.exists():
        info = path.read_text()
        name = json.loads(info)
        print(f"Hello, again, {name}!")
    else:
        name = input("Hi, please introduce yourself! ")
        info = json.dumps(name)
        path.write_text(info)
        print(f"We saved your name, {name}!")

say_hello()

# now let's refactor say_hello, since it's doing so much already:
# make code for retrieving stored name, an independent function.

from pathlib import Path
import json

def get_stored_name(path):
    """Get stored name if it exists."""
    if path.exists():
        info = path.read_text()
        name = json.loads(info)
        return name
    else:
        return None

def say_hello():
    """Say hello with user's name."""
    path = Path('name.json')
    name = get_stored_name(path)
    if name:
        print(f"Hi {name}, again!")
    else:
        name = input("Introduce yourself, please. ")
        info = json.dumps(name)
        path.write_text(info)
        print(f"We saved your name, {name}!")

say_hello()

# factor code for say_hello():
# if name doesn't exist, make a function that prompts for a new name:

from pathlib import Path
import json

def get_stored_name(path): # retrieves stored name if exists.
    """Get stored name if it exists."""
    if path.exists():
        info = path.read_text()
        name = json.loads(info)
        return name
    else:
        return None

def say_hello():
    """Say hello with user's name."""
    path = Path('name.json')
    name = get_stored_name(path)
    if name:
        print(f"Hi {name}, again!")
    else:
        name = input("Introduce yourself, please. ")
        info = json.dumps(name)
        path.write_text(info)
        print(f"We saved your name, {name}!")

def get_new_name(path):
    """ask for a new name."""
    name = input("Please introduce yourself. ")
    info = json.dumps(name)
    path.write_text(info)
    return name

def say_hello(): 
    """Say hello to the user with their name."""
    path = Path('name.json')
    name = get_stored_name(path)
    if name:
        print(f"Hello, {name}, it's great to have you back!")
    else:
        name = get_new_name(path)
        print(f"We'll save your name for next time, {name}!")

say_hello()
