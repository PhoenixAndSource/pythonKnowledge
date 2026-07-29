# exceptions are special objects that manage errors during a program's execution.
# when an error happens/ or when Python doesn't know what to do with the error,
# Python makes an exception object

# write code to handle exceptions so that the program will keep running.
# otherwise the program will show a traceback, with the exception

# use try-except blocks to handle exceptions.
# these will show users your custom friendly error messages 

## Handling the ZeroDivisionError Exception

# let's ask python to divide a number by zero.

# print(5/0)

# Traceback (most recent call last):
#    File "division_calculator.py", line 1, in <module>
#        print(5/0)

# ZeroDivisionError: division by zero 

# ZeroDivisionError is an exception object.
# this is an example of Python stopping the program,
# and telling us what type of exception was found.
# we use this info to modify our program,
# by telling Python what to do when this happens.

## Using try-except Blocks

try: 
    print(5/0) # this is inside a try block
except ZeroDivisionError:
    print("You can't divide by zero!")

# If the try block works, Python skips the except block which is the exception
# if the code in the try block results in an error, 
# Python looks for the except block that matches the error raised, 
# and run the code in that block.

## Use Exceptions to Prevent Crashes
# calculator that does division only:
# program does not handle errors, so dividing by zero makes it crash

print("think of two numbers to divide here.")
print("enter 'quit' to quit.")

while True:
    your_number = input("\nYour number: ")
    if your_number == 'quit':
        break
    your_other_number = input("Your other number: ")
    if your_other_number == 'quit':
        break
    answer = int(your_number) / int(your_other_number)
    print(answer)

## the else Block

print("think of two numbers to divide here.")
print("enter 'quit' to quit.")

while True:
    your_number = input("\nYour number: ")
    if your_number == 'quit':
        break
    your_other_number = input("Your other number: ")
    if your_other_number == 'quit':
        break

    try:
        answer = int(your_number) / int(your_other_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    except ValueError:
        print("Please enter valid numbers only!")
    else:
        print(answer)

# This way the program keeps running, and the user doesn't see a traceback.
