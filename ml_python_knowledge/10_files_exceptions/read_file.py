## path is location of file or folder
# python has a module called pathlib 
# that works with any operating system or program.
# this type of module that has the above functionality 
# is called a library.

# In this example, we import the class Path from pathlib.

# things you can do with a Path object that points to a file:
# 1. check if a file exists
# 2. read the file contents
# 3. write new data to the file.

# Let's create a Path object that represents pi_numbers.txt
# assigning it to the path variable.

# The file needs to be saved, sharing 
# the same directory as this file, read_file.py.

from pathlib import Path

path = Path('pi_numbers.txt')
contents = path.read_text()
print(contents)

# After we have the pi_numbers.txt,
# We use the read_txt() method to read all of the file.
# which we assign a variable contents 
# to the string of the content that is returned.

# when we print it, there will be a blank line after the content,
# so let's use rstrip() on contents

from pathlib import Path

path = Path('pi_numbers.txt')
contents = path.read_text()
contents = contents.rstrip()
print(contents)

# we can also strip the trailing newline character after it reads contents
# with rstrip right after read_text():

from pathlib import Path

path = Path('pi_numbers.txt')
contents = path.read_text().rstrip()
print(contents)

# this is an example of method chaining:
# contents = path.read_text().rstrip() 
# so Python does the read_text() method,
# then uses rstrip() method to the 
# string of content that read_text() returns.
# this new string is then assigned to variable contents.

## Relative and absolute paths
# Relative path: python follow given 
# location relative to the directory of current running program.

## Relative & Absolute File Paths
# example of relative file path:
path = Path('phoenix_files/phoenix.txt')

# Absolute paths start at system's root folder:
# example of absolute path:
path = Path('Users/username/Desktop/ml_python_knowledge/phoenix_files/phoenix.txt')

## Access a File's Lines
# using splitlines() method: 
# from a long string transformed into a set of lines,
# for loop to read each line from a file
# note: if you are just using individual lines, you don't need to use rstrip().

from pathlib import Path

path = Path('pi_numbers.txt')
contents = path.read_text()

lines = contents.splitlines() # splitlines() method returns a list of all lines from file.
for line in lines: # from the list, we assign the list the variable lines.
    print(line) # loop the lines, and print each line.

# output is the same as original text file, since we made no modifications.

## Use File's Contents
# make a single string with all digits in file with no blank lines.

# pi_string_digits.py
