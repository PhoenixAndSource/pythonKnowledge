# here are styling conventions:

# functions and module names should have: descriptive names, lowercase letters, & underscores.
# functions should include comments that clearly explain what the code is trying to accomplish.
# the comment should be right after the function definition, and use the docstring format.

# test that it is well-documented:
# can another programmer trust that the code works as explained,
# the function name
# the arguments needed
# type of value it returns
# can another programmer use it in their program?

# a parameter's default value should not have spaces around the equal sign:
def function_example(parameter_0, parameter_1='default value')

# keyword arguments in function calls:
function_example(value_0, parameter_1='value')

#PEP 8 recommends 79 characters of code max per line.
# if set of parameters in function's definition is longer than 79 characters, 
# press ENTER after opening parenthesis on the definition line. 
# next line, press TAB key 2 times to separate list of arguments from body of the function(which is only indented once.)

def function_example(
        parameter_0, parameter_1, parameter_2,
        parameter_3, parameter_4, parameter_5):
    function body...

# if program or module has multiple functions,
# separate them with two blank lines for legibility.
# import statements are placed at the beginning of a file,
# except for if you leave comments at the beginning of your file to explain the whole program.
