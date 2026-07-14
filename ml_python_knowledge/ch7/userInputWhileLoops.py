## input() function
# while loop keeps programs running, while under a specific circumstances

# input() stops the program, while waiting for user to do something.

letter = input("Write a letter to Santa, and here is your letter to Santa: ")
print(letter)

# user sees "Write a letter to Santa, and here is your letter to Santa:"
# program waits for user to type a letter.
# when user taps ENTER, the program continues with the programmed response that is tied to variable letter.
# program prints the input for the user to see.

# input() instructions should be clear to the user.
# at the end of your instructions to the user, add a space,
# so it makes a clear distinction between your instructions or prompt, and your users' input
# and so it shows the user where to type their input.

your_name = input("Write your name: ")
print(f"\nHowdy, {your_name}!")

# for multiple line prompts, or a multiline string.
# assign prompt to variable and allow input() function to use it.
# This prompt uses two lines, and we also put a space after the second string so there is clarity between the user input and the instructions.

instructions = "Hi, I'll like to refer to you personally, with your name." # this part of message is associated with this prompt
instructions += "\nWhat would you like to be called? " # the operator += uses the above string that is associated with prompt, and adds this string after it.

yourName = input(instructions)
print(f"\nHi, {yourName}!")

## int() allows numerical input
# input() function reads the input as a string.

age = input("What is your age? ")
age = int(age)
if age >= 18:
    print("You're an adult.")
else:
    print("You're still a child.")


# using int() in a program:

stickMeasurement = input("How tall is the branch? ")
stickMeasurement = int(stickMeasurement)

if stickMeasurement >= 20:
    print("\nIt's perfect as a garden stake!")
else:
    print("\nIt would be okay if we used it as a fishing pole!")


