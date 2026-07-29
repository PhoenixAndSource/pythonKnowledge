# write_text() method:
# takes the argument which is the string you write to the file.
# this program has no terminal output.
# you can see it in love_letter.txt

# we'll store it in a file
# we won't print it.

from pathlib import Path

path = Path('love_letter.txt')
path.write_text("I love you Phoenix.")

# writing multiple lines

from pathlib import Path

contents = "I love you. \n" # define variable called contents that holds all content of file.
contents += "I enjoy life with myself\n" # += operator adds to the string.
contents += "I enjoy my fulfilling career that maintains and grows my wealth and freedom in my life.\n" # += keep using this operator to add to string.
# newline characters make sure each statement lives on its own line.
# length of strings is unlimited.

path = Path('love_letter.txt')
path.write_text(contents)



