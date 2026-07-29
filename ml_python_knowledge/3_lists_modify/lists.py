# list examples: alphabet letters, numerical digits, names of people in a group
# square brackets [] means list in python.

mlspokenlanguages = ['cantonese', 'mandarin','english','french']
print(mlspokenlanguages)

# python will print the list, showing the list with the square brackets

# to get any item in the list:
# write the list name, with the index of the item, inside square brackets.

mlspokenlanguages = ['cantonese', 'mandarin', 'english', 'french']
print(mlspokenlanguages[0])

# you can use string methods on items in the list
# for example: format 'cantonese' using title() to capitalize it.

mlspokenlanguages = ['cantonese', 'mandarin', 'english', 'french']
print(mlspokenlanguages[0].title())

# index positions start at 0, not 1 

mlspokenlanguages = ['cantonese', 'mandarin', 'english', 'french']
print(mlspokenlanguages[1])
print(mlspokenlanguages[3])

# This prints mandarin (the second item), and french (the fourth item).

mlspokenlanguages = ['cantonese', 'mandarin', 'english', 'french']
print(mlspokenlanguages[-1])

# [-1] will return french. 
# -1 always returns the last item on the list.
# -2 returns second to last item. in otherwords, the second item from the end of the list.
# -3 returns the third from fro the end. etc.

mlspokenlanguages = ['cantonese', 'mandarin', 'english', 'french']
message = f"ML speaks and writes in {mlspokenlanguages[3].title()} fluently."

print(message)
