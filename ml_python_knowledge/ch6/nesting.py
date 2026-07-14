## examples of nesting:
# dictionaries in a list
# list of items as a value in a dictionary
# a dictionary inside a dictionary

# here are three dictionaries:

iceCream_0 = {'flavour': 'strawberry', 'scoops': '3'}
iceCream_1 = {'flavour': 'blueberry', 'scoops': '5'}
iceCream_2 = {'flavour': 'acai', 'scoops': '8'}

# we store these dictionaries in a list called iceCreamCones.

iceCreamCones = [iceCream_0, iceCream_1, iceCream_2]

for iceCream in iceCreamCones:
    print(iceCream)

# here we'll make 6 ice cream cones.

# here is an empty list:
iceCreamCones = []

# make 6 ice cream cones.
for iceCreamCone_number in range(6):
    new_iceCreamCones = {'flavour': 'lychee', 'scoops': '1', 'cone': 'waffle'}
    iceCreamCones.append(new_iceCreamCones)

# Show the first 3 ice cream cones,
for iceCream in iceCreamCones[:3]:
    print(iceCreamCones)
print("...")

# Show how many ice cream cones have been scooped.
print(f"I finished making {len(iceCreamCones)} ice cream cones!")

## add a for loop and if statement to change the flavour of the ice cream cones:

# make an empty list for ice cream cones.
iceCreamCones = []

# make 3 lychee ice cream cones.
for iceCreamConeNumber in range (3):
    newIceCreamCone = {'flavour': 'lychee', 'scoops': 3, 'cone': 'waffle'}
    iceCreamCones.append(newIceCreamCone)

for iceCream in iceCreamCones[:2]:
    if iceCream['flavour'] == 'cherry':
        iceCream['flavour'] = 'lychee'
        iceCream['cone'] = 'waffle'
        iceCream['scoops'] = 3

# output the first 3 ice cream cones.
for iceCream in iceCreamCones[:5]:
    print(iceCream)
print("...")

## you could expand this loop by adding an elif block that turns lychee order into cherry, and scoops from 2 to 3 scoops
for iceCreamConeNumber in range (3):
    newIceCreamCone = {'flavour': 'lychee', 'scoops': 3, 'cone': 'waffle'}
    iceCreamCones.append(newIceCreamCone)

for iceCream in iceCreamCones[0:3]:
    if iceCream['flavour'] == 'lychee':
        iceCream['flavour'] = 'cherry'
        iceCream['cone'] = 'waffle'
        iceCream['scoops'] = 2
    elif iceCream['flavour'] == 'lemon':
         iceCream['flavour'] = 'orange creamsicle'
         iceCream['cone'] = 'taco waffle'
         iceCream['scoops'] = 3

for iceCream in iceCreamCones:
    print(iceCream)

# A List in a Dictionary
# put info about an ice cream order.

iceCream = {
    'iceCreamBase': 'soy',
    'toppings': ['cacao', 'cinnamon'],
    }

# print the order
print(f"Your {iceCream['iceCreamBase']} ice cream order is ready!" 
      "with your favourite toppings: ")

for topping in iceCream['toppings']:
    print(f"\t{topping}")

# favorite drinks: inside dictionary's for loop, another for loop runs through favorite drinks:

favoriteDrinks = {
    'jupiter': ['chamomile', 'green tea'],
    'sacredmoon': ['moon water'],
    'angel': ['matcha', 'magic purity water'],
    'buddha': ['chai', 'mango'], 
    }

for name, drinks in favoriteDrinks.items():
    print(f"\n{name.title()}'s ready for:")
    for drink in drinks:
        print(f"\t{drink.title()}")


## A dictionary within a dictionary exaxmple:

artists = {
    'amazoniangoddess': {
        'firstname': 'amazon',
        'lastname': 'goddess',
        'goddessaffiliation': 'birds of the forest',
        },

    'surflove': {
        'firstname': 'catch',
        'lastname': 'waves',
        'goddessaffiliation': 'sandy beach',
        },

}

for artists_username, artist_info in artists.items():
    print(f"\nArtist Username: {artists_username}")
    full_artist_name = f"{artist_info['firstname']} {artist_info['lastname']}"
    goddessaffiliation = artist_info['goddessaffiliation']

    print(f"\tFull artist name: {full_artist_name.title()}")
    print(f"\tAffiliation: {goddessaffiliation.title()}")


