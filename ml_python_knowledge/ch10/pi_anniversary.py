from pathlib import Path

path = Path('pi_unlimited_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string_digits = ''
for line in lines:
    pi_string_digits += line.strip()

anniversary = input("Write in your anniversary, in this format mmddyy: ") # prompt anniversary date
if anniversary in pi_string_digits: # check if it is in pi_string_digits
    print("Your anniversary digits appear in the first 2 million of pi!")
else:
    print("Your anniversary digits does not appear in the first 2 million of pi!")
