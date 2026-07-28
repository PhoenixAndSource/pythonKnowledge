# store functions in separate file called module,
# then import that module into your main program.
# import statement tells Python to use the code in the module with the current program.

## Import Entire Module
# a module is a file that ends in .py that has the code you want to import into your program.

# make a module that contains function create_magic().

# code for magic.py
def create_magic(numberBreaths, *magic_items):
    """Describe the magic we are creating."""
    print(f"\nCreating a {numberBreaths}breaths with these magic items:")
    for magic_item in magic_items:
        print(f"- {magic_item}")

# code creating_magic.py
import magic

magic.create_magic(3, 'laptop')
magic.create_magic(1, 'perseverance', 'prayer', 'meditation', 'persistence in actionable steps towards my dream life')

# import tells Python to open magic.py, and copy all functions from it into the present program. 
# it doesn't show code being copied, but Python will copy it before running the program.
# any function in magic.py will be available to be used in creating_magic.py

# call a function from imported module:
# write the name of the imported module, magic, 
# then the name of the function, create_magic()
# use a dot to separate.

# this is the syntax to import an entire module named module_example.py
# module_example.function_name()


## Import Specific Functions
from module_example import function_example

# get unlimited functions from a module with a comma to separate each function:
from module_example import function_0, function_1, function_2

# creating_magic.py example
from magic import create_magic

create_magic(2, 'perserverance')
create_magic(1, 'faith', 'meditation', 'prayer', 'study')

## Alias for Function
# here alias for create_magic() will be cm(), by importing create_magic as cm.
# as keyword renames function using the alias you assign it.
# syntax for creating an alias is 
from module_example import function_example as fe

# magic example:
from magic import create_magic as cm

cm(2, 'faith')
cm(1, 'love', 'self-love', 'self-protection')


## Import Every Function into a Module
# by using the asterick (*) operator
# * tells Python to copy every function from module magic to program file
# you don't need to use the dot notation, since every function is imported, 
# you can call functioins by name.
# doesn't work as well with large modules you didn't create
# usually you import desired functions, or import entire module and use dot notation.
# example:
from module_example import *

# magic example:
from magic import *

create_magic(2, 'faith')
create_magic(1, 'self-love', 'happiness', 'self-discipline')

