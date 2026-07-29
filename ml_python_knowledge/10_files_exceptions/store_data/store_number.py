from pathlib import Path
import json # import json module

list_numbers = [7, 88, 86, 10, 15] # create list of numbers

path = Path('list_numbers.json') # make filename to store list of numbers
contents = json.dumps(list_numbers) #json.dumps() is a function to create a string that encompasses our data in JSON format.
path.write_text(contents) # we write to the file with this string

# program produces no output, however, it will appear in list_numbers.json
