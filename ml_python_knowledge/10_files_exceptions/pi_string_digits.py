from pathlib import Path

path = Path('pi_numbers.txt') # create a Path object for the file
contents = path.read_text() # read entire file as a string

lines = contents.splitlines() # split the file contents into a list of lines
pi_string_digits = '' # initialize an empty string to store all digits
for line in lines: # iterate through each line
    pi_string_digits += line # connect each line to the digit string.

print(pi_string_digits) # print all digits of the representation of pi
print(len(pi_string_digits)) # print the total count of digits

# note: txt files are interpreted as strings.
# to interpret the values numerically, 
# use int() function to turn it into an interger
# or use float() function to turn it into a float.

## Large files with unlimited digits

from pathlib import Path

path = Path('pi_unlimited_digits.txt') # create a Path object for the file
contents = path.read_text() # read entire file as a string

lines = contents.splitlines() # split the file contents into a list of lines
pi_string_digits = '' # initialize an empty string to store all digits.
for line in lines: # iterate through each line
    pi_string_digits += line.lstrip() # remove leading whitespace and concatenate to digit string.

print(f"{pi_string_digits[:53]}...") # print first 53 digits of pi
print(len(pi_string_digits)) # print total count of digits

# Python allows you to work with unlimited amount of data
# however, it just depends on your system's memory capacity.
