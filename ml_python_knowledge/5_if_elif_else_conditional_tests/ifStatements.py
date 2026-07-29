## If Statements

# If statements allow specific situations to be handled specifically.

affirmations_of_love = ["i am worthy", "xoxo", "i am loved", "i am enough"]

for kisses in affirmations_of_love:
    if kisses == "xoxo":
        print(kisses.upper())
    else:
        print(kisses.title())

## Conditional Tests
# Check for Equality with Strings

kisses = "xoxo"
if kisses == "xoxo":
    print("True")
else:
    print("False")

# Equality using == operator is case sensitive

kisses = "XOXO"
if kisses == "xoxo":
    print("True")
else:
    print("False")

kisses = "XOXO"
if kisses.lower() == "xoxo":
    print("True")
else:
    print("False")

# This type of conditional test is useful when you want to make sure all usernames are unique regardless of case, by converting the newly submitted username to lowercase, and checking all lowercase usernames in existing database to make sure the new name is unique before allowing the new username to be submitted.

## Check for Inequality - comparing two values with the inequality operator (!=)

# example
# 1. store value in a variable
# 2. print message if not equal.

recipe_list = 'jellyfish'

if recipe_list != 'jellyfish':
    print("The recipe does not call for Jellyfish!")

# the code sees if the value of recipe_list is the same or different to the value 'jellyfish'.
# If the vales are not the same, Python deems it True and responds with the code after the if statement.

# if the values are the same, Python will determine it False, so it will not use the code that comes after the if statement.
# Since the value of recipe_list is not "jellyfish", the print() function activates:
# The recipe does not call for Jellyfish!

# test equality when matches are important
# test inequality when non-match is usually expected and more common in the situation
# test inequality when you know what you want/ intend
# test for inequality for readability and to maintain easily.
# test for inequality for fewer operations and better branching, avoid multiple comparisons



## Compare numerical values

# check age if someone is 16:

age = 16
is_sixteen = (age == 16)
print(is_sixteen)

# check if two numbers not equal
numberOfPinkPenguins = 13
if numberOfPinkPenguins != 45:
    print("that is the number of tuxedo penguins waddling around after the eggs hatch, "
    "not the current number of tuxedo penguins.")

# mathematical comparisons

age = 15
age < 30

# True

age <= 21

# True

age > 21

# False

age >= 21

# False


# Check Multiple Conditions
# check if both conditions are true simultaneously by using keyword and to combine

age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >=21

# False

age_1 = 22
age_0 >= 21 and age_1 >= 21

# True

# or is a keyword to check multiple conditions:

age_0 = 5
age_1 = 30
age_0 >= 15 or age_1 >= 20

if age_0 >= 1 or age_1 >= 35:
    print("True")
else:
    print("False")

age_0 =50
if age_0 >= 60 or age_1 <= 30:
    print("True")
else:
    print("False")

# Check if a value is in a list with "in"

affirmations = ['love', 'pat on the back', 'high kick in the air']
if 'pat on the back' in affirmations:
    print("in the list")
else:
    print("not in list")

if 'fresh juice in the morning' in affirmations:
    print('in the list')
else: 
    print('not in the list')

# Check if value is not in list with "not in"

partyInvitations = ['jack', 'girlfriend', 'mom']
invitees = 'dad'
if invitees not in partyInvitations:
    print(f"{invitees.title()}, you are not on the list. You may request an invitation.")


## Boolean Expressions

# A boolean expression is a conditional test that outputs True or False.
# Boolean values monitors if a game is active, or if a writer can edit a page.

user_actively_playing = True
edit_allowed = False


## "if" Statements

age = 16
if age >= 16:
    print("You can get a license to drive.")
    print("Have you studied for the licensing test?")
    
# if-else Statements
age = 13
if age >= 16:
    print("You can test for a license to drive.")
else:
    print("You need to wait until you are 16 or older to get an appointment to test for a driver's license.")


## "if-elif-else" is if you have more than two situations.
# python runs one block of code
# python runs the first test, and the next, all in order, until one of the test passes.
# the code that passed is the code that python will execute.
# python will ignore the rest of the tests and its codes.

age = 50
if age < 34:
    print("You're still young.")
elif age < 70:
    print("You can still live a good life.")
else:
    print("It's always a good time to rest, but don't forget to live your best life.")

# more efficient

age = 20

if age < 5:
    instruments = 2
elif age < 12:
    instruments = 3
else:
    instruments = 5

print(f"You are most like to be proficient in at least {instruments}.")

## Omitting the else Block, and using the elif block to be specific about the last test.
# whereas the else block is a general test for all the situations, besides the elif block, that is for a specific situation.

age = 20

if age < 5:
    instruments = 2
elif age < 12:
    instruments = 3
elif age >= 12:
    instruments = 1

print(f"You are most like to be proficient in at least {instruments}.")

## Test Multiple Conditions

# if-elif-else good for one test, but ignores the rest of the tests.

# if you want to use all situations that tests True, you can use a bunch of if statements, with no elif or else blocks.
# you would use it if there are multiple tests that would be True, and you want to use all the tests that tested True.

affirmations = ['love', 'happiness', 'peace']

if 'love' in affirmations:
    print("I Am Loved.")
if 'happiness' in affirmations:
    print ("I am truly happy.")
if 'wealthy' in affirmations:
    print ("I am ready to be wealthy.")
if 'peace' in affirmations:
    print ("I finally found Peace. thank you!")

print("\nAmen. I love you.")

# if-elif-else block would not work because the code would stop running after one test passes.

affirmations = ['love', 'happiness']

if 'love' in affirmations:
    print("I found Love.")
elif 'wealth' in affirmations:
    print("Forever wealthy.")
elif 'happiness' in affirmations:
    print("I Am ready to be wealthy and happy.")

print("\nAnd so it is. Thank you from the bottom of my heart. <3")

# if you desire only one block of code to execute, use if-elif-else block.
# if you need more than one block of code to be output, use independent if statements, sans elif and else blocks. Thank you.













