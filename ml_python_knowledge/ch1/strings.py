# string in Python, is a series of characters inside of both single and double quotes

print("ml demonstrates printing a string.")

message = "ml demonstrates creating a message from a string to be printed later."
print(message)

mllovesrainbowsmessage = "ml loves rainbows."
print(mllovesrainbowsmessage)

# changing lowercase to uppercase and vice versa, inside a String, using Methods

capitalcity = "hong kong"
print(capitalcity.title())
print(capitalcity.upper())
print(capitalcity.lower())

# lower() is helpful for changing user input to
# all lowercase to store data,
# then you can choose the appropriate case to display later.

# Variables in Strings
# using a variable's value inside a string
# Displaying full name using two variables:
# one to represent the given name,
# and the second to represent the last name,
# then put the two values together.

given_name = "most"
last_name = "loved"
full_name = f"{given_name} {last_name}"
print(full_name)
print(f"Ciao, {full_name.title()}!")

# Add Whitespace to Strings
# Using Tabs or Newlines

# add whitespace using tabs \t
print("Poem")

print("\tPoem")

# add whitespace using newline \n

print("Poems: \nI'm not dead yet\nShould I be?\nAngels answer the call")

# combine tabs and newlines in a single string
# \n\t is new line, and then next line with a tab.

print("True Poems: \n\tI love myself\n\tI am loved by the universe\tI am so loved. ")

# stripping whitespace

# strip whitespace from right
practicepythonmessage = "ml practices writing python "
practicepythonmessage = practicepythonmessage.rstrip()
print(practicepythonmessage)

# strip whitespace from left

removeLWhitespace = " ml practices removing whitespace with python's 'lstrip()'"
removeLWhitespace = removeLWhitespace.lstrip()
print(removeLWhitespace)

# strip whitespace from both left and right.

removeWhitespace = " ml removes whitespace "
removeWhitespace = removeWhitespace.strip()
print(removeWhitespace)

# removing prefixes

cherrybombagency_url = "https://cherrybombagency.com"
cherrybombagency_url = cherrybombagency_url.removeprefix("https://")
print(cherrybombagency_url)
