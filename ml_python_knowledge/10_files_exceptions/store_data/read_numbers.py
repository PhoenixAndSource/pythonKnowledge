# example of sharing data between files!!!

from pathlib import Path
import json

path = Path('list_numbers.json')
contents = path.read_text() # read content with read_text() method
list_numbers = json.loads(contents) # pass contents to json.loads()
# which takes the string in the JSON format, 
# and returns a Python object which is a list here.
# then assign to list_numbers.
print(list_numbers) # print the numbers which are from the list in store_numbers.py


