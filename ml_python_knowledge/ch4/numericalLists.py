# numerical lists stores a group of numbers.
# examples in data visualizations:
# temperatures,
# distances,
# population sizes,
# latitude & longitude values

# range() function
# generates a series of numbers

for numbers1234 in range(1, 5):
    print(numbers1234)

# it prints, 1,2,3,4 but doesn't print 5. range() here prints only numbers 1-4.
# python interprets range() to start counting at the first value you inputted, then stops at the second value you inputted.
# so to print 1-5 or 1,2,3,4,5, you need to use range(1,6)

for numbersonethroughfive in range(1, 6):
    print(numbersonethroughfive)

# range(6) would give you 0-5

for zeroto5 in range(6):
    print(zeroto5)

# use range to make a list of numbers
numbers = list(range(1, 6))
print(numbers)

# even numbers 1 though 10.
# here we start with 2 then we add 2 to each next number
# until we reach the end value that we gave it which was 11,
# which makes [2,4,6,7,10]
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# Square numbers
# two asterisks ** symbolize exponents in Python.
# an example of a list of the first 10 square numbers:

squares = []  # squares is an empty list
for value in range(
    1, 11
):  # tell python to loop through from 1-10 using the range() function.
    square = (
        value**2
    )  # inside the loop, the current value is raised to the second power, and assigned to the variable square.
    squares.append(square)  # each new value of square is appended to the list squares.
    # append() method builds lists by starting with an empty list, then adding items using append() calls.

print(squares)  # when the loop has stopped running, the list of squares is printed.

# it prints [1,4,9,16,25,36,49,64,81,100]

# You can also simply append each new value directly into the list:

squarednumbers = []
for value in range(1, 11):
    squares.append(value**2)

print(squares)


## Statistics with a List of Numbers
# find the minimum, maximum and sum of a list of numbers

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

# A List Comprehension gives you the ability to produce list with simply one line of code.
# it combines the for loop, creates new items into one line, appends each new item.

squares = [value**2 for value in range(1, 11)]
print(squares)

tripleexponentlistcomprehensiontry = [value**3 for value in range(0, 4)]
print(tripleexponentlistcomprehensiontry)
