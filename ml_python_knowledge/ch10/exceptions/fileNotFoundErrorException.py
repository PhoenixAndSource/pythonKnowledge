## fileNotFoundErrorException
# handles missing files
# 1. file may be in a different place
# 2. filename may be spelled differently
# 3. file may not exist.

# here is an example of a program attempting to read 
# a file that doesn't exist.

# from pathlib import Path

# path = Path('wrong_order.txt')
# contents = path.read_text(encoding='utf-8')

# encoding argument is needed when 
# system's default encoding is not the same 
# as the encoding of current file being read.
# usually happens when reading a file created on a different system

# Python raises an exception to the missing file with a traceback
# that says FileNotFoundError.

from pathlib import Path

path = Path('wrong_order.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")


## Analyzing Text

from pathlib import Path

path = Path('the_giving_tree.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
else:
    # Count the approximate number of words in the file:
    words = contents.split()
    num_words = len(words)
    print(f"The file {path} has about {num_words} words.")

# the_giving_tree.txt is now in the correct directory, so the try block will work this time.
# take string contents which now has all the text in the giving tree in a single string
# use split() to make a list of all the words in the book.
# len() on the list shows us the number of words in book.