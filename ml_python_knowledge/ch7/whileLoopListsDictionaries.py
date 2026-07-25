## lists and dictionaries for dealing with data in a while loop

# list unverified cats
# empty list holds verified cats

unverified_cats = ['peppy', 'loki', 'pretty']
verified_cats = []

# verify all cats by moving/ transforming unverified cats into list of verified cats.

while unverified_cats:
    now_cat = unverified_cats.pop()

    print(f"Verifying cat: {now_cat.title()}")
    verified_cats.append(now_cat)

# show all verified cats.
print("\nThese cats have now been verified:")
for verified_cat in verified_cats:
    print(verified_cat.title())

# try on my own.
# list unverified users
# make an empty list/ container for verified users.
unverified_users = ['happy', 'miss Beautiful', 'pretty sexy']
verified_users = []

while unverified_users:
    current_user = unverified_users.pop()

    print(f"Verifying new user: {current_user.title()}")
    verified_users.append(current_user)

# show all verified users:
print("\nThese users are now verified:")
for verified_user in verified_users:
    print(verified_user.title())

## Try test 2

# first list the unverified users
# then, make an empty list for the verified users.

unverified_users = ['happy', 'gorgeous', 'pretty sexy']
verified_users = []

# then show the unverified users

while unverified_users:
    current_user = unverified_users.pop()

    print(f"These users are unverified: {current_user.title()}")
    verified_users.append(current_user)

# show all verified users:
print("\nThese users are now verified:")
for verified_user in verified_users:
    print(verified_user.title())

# Test 2

# first list unverified users
# then make an empty list for verified users

unverified_users = ['educated', 'successful', 'graduated with masters degree']
verified_users = []

# then we print unverified users

while unverified_users:
    current_user = unverified_users.pop()

    print(f"These users are unverified: {current_user.title()}")
    verified_users.append(current_user)

# show all verified users:

print(f"These are all the verified users:")
for verified_user in verified_users:
    print(verified_user.title())

## Test 3 
# first we list all the unverified users
# then we make an empty list for verified users.

unverified_users = ['graduated with masters degree in artificial intelligence', 'graduated with masters degree in electrical engineering', 'got amazing well-paying job and career with career accolades and much celebration and success!']
verified_users = []

# print unverified users

while unverified_users:
    current_user = unverified_users.pop()

    print(f"These users are unverified: {current_user.title()}")
    verified_users.append(current_user)

# move unverified_users to verified_users and print the list of verified users.

print(f"These are all the verified users:")
for verified_user in verified_users:
    print(verified_user.title())    


## In list, remove all instances of specific values

stuffies = ['bunny', 'bird', 'mermaidcat']
print(stuffies)

while 'bunny' in stuffies:
    stuffies.remove('bunny')

print(stuffies)

## Fill dictionary with user input

responses = {}
# sign that polling is happening.
polling_happening = True
while polling_happening:
    # ask for the user's name and response
    name = input("\nWhat is your name? ")
    response = input("Where would you like to go? ")

    # make a dictionary to store the response.
    responses[name] = response

    # Find out if anyone else wants to take the poll.
    repeat = input("Does anyone else like to respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

    # Polling is done. Print the results.
    print("\n-- Poll Results --")
    for name, response in responses.items():
        print(f"{name} would like to go to {response}.")



