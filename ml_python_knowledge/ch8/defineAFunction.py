# def means you're defining a function (a function definition)
# def tells python the name of the function.
# the parentheses holds the action of the function.
# these parentheses are empty, because the function doesn't need any info for it to show "Hello".
# definition ends in a colon.

def say_hello(): # say_hello only has one job which is to print("Hello").
    """Show the hello.""" # this is a docstring, which shows what the function does.
    print("Hello") # this is the only code in the function.

say_hello()

## Pass Info to a Function
# say hello to the user with their name.
# username below is an example of a parameter. it's info that the function needs to do its job.
# say_hello(MimiIsLoved) is an example of an argument. an argument is info that's passed from a function call, to a function. 

def say_hello(username):
    """Show the hello"""
    print(f"Hello, {username.title()}!")

say_hello('Best Actress')

## Positional Arguments

# if you call a function,
# Python finds the corresponding argument in the function call with the parameter.
# Here is a function that shows info about stuffies:

def stuffie_info(type_animal, stuffie_name):
    """Show info about stuffie."""
    print(f"\nI have a {type_animal}.")
    print(f"I named my {type_animal}, {stuffie_name.title()}.")

stuffie_info('bunny', 'cutie-patootie')

## Multiple Function Calls
# you can call as many times as you like.

def stuffie_info(type_animal, stuffie_name):
    """Show info about stuffie."""
    print(f"\nI have a {type_animal}.")
    print(f"My stuffie is a {type_animal}, and its name is {stuffie_name.title()}.")

stuffie_info('bunnysocute', 'bunnyunicornsopretty')
stuffie_info('prettyGirlturtle', 'turtleangelfish')

## pay attention to order in Positional Arguments
def stuffie_info(type_animal, stuffie_name):
    """Show info about stuffie."""
    print(f"\nMy stuffie is a {type_animal}.")
    print(f"I named my {type_animal}, {stuffie_name.title()}.")

stuffie_info('fluffy rabbit', 'bunnylove')

## Keyword Arguments
# name-value pair that passes to a function.
# order doesn't matter, since the arguments and parameters are paired.

def stuffie_info(type_animal, stuffie_name):
    """Show info about stuffie."""
    print(f"\nThe type of stuffie I have is a {type_animal}.")
    print(f"I named my {type_animal}, {stuffie_name.title()}.")

stuffie_info(type_animal='bunny', stuffie_name='happybabybunny') #bunny is the argument, parameter is type_animal.

## Default Values
def stuffie_info(stuffie_name, type_animal='cutebunny'):
    """Show stuffie info."""
    print(f"\nThis stuffie is a {type_animal}.")
    print(f"My {type_animal} is named {stuffie_name.title()}.")

stuffie_info(stuffie_name='bunnylovelove')

#another function call:
#explicit argument for type_animal, python will ignore default value 'cutebunny' as an example.

stuffie_info(stuffie_name='kitteny', type_animal='cat')

## Equivalent Function Calls

#in this definition, you always need an argument for stuffie_name. 
# you can use a positional or keyword format.
def stuffie_info(stuffie_name, type_animal='bunny'):
    """Show stuffie info."""
    print(f"My stuffie type is {type_animal}, and its name is {stuffie_name}")

#a cat named Kitteny.
stuffie_info('kitteny')
stuffie_info(stuffie_name='kitteny')

#a bird named PrettyBird.
stuffie_info('prettyBird', 'bird')
stuffie_info(stuffie_name='prettyBird', type_animal='bird')
stuffie_info(type_animal='bird', stuffie_name='prettyBird')

## Avoiding Argument Errors

# this example shows information missing

def stuffie_info(type_animal, stuffie_name):
    """Show stuffie info."""
    print(f"\nMy stuffie type is {type_animal}")
    print(f"My {type_animal} is named {stuffie_name.title()}")

stuffie_info()

# terminal shows the error:     
# stuffie_info()
#  ~~~~~~~~~~~^^
# TypeError: stuffie_info() missing 2 required positional arguments: 'type_animal' and 'stuffie_name'