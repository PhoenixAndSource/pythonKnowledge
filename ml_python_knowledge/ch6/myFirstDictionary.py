## dictionaries store values for specific items.

myDreamLife = {'freedom': 'safety'}

# another example:

livingMyDreams = {'home': 'safety', 'money': 333_333_333}

print(livingMyDreams['home'])
print(livingMyDreams['money'])

# if using Terminal, it should output: 
# safety
# 333333333

## dictionaries in Python are key-value-pairs.
# a key is associated with a value,
# The value can be: any object you create in Python
# ie: number/string/list/another dictionary

# a dictionary is inside braces ({})
# inside the braces, is a collection of key-value-pairs

livingMyDreams = {'home': 'safety', 'money': 333_333_333}

# keys are paired with values with a colon.
# independent key-value pairs isolate from eachother with a comma.

# there is no limit to how many key-value pairs within a dictionary.

# To Access the values in the dictionary, 
# put the key inside square brackets.
# The dictionary is myDreamsHaveComeTrue,
# the key is 'mood'
# the value is 'content'

myDreamsHaveComeTrue = {'mood': 'content'}
print(myDreamsHaveComeTrue['mood'])

# the output is the value connected to the key 'mood' from the dictionary myDreamsHaveComeTrue.
# the output is 'content'

# python allows an infinite number of key-value pairs in a dictionary.
# here's an example of a dictionary containing two key-value pairs:

myDreamsAreNowTrue = {'IAmWorthyAndSuccessful': 'I am successful in all the best ways for me', 'IAmHappy': 'Finally, all the pieces of my true and best dream life have come together for me'}

myContentmentAndHappiness = myDreamsAreNowTrue['IAmHappy']
print(f"This is my new life: {myContentmentAndHappiness}, finally!")

myWealthAndStabilityIsGreat = myDreamsAreNowTrue['IAmWorthyAndSuccessful']
print(f"Also, {myWealthAndStabilityIsGreat} is also part of my reality, now.")

IMakeTheBestDecisionsForMyMostAbundantDreamLife = {'contentment': 'living with my children'}
print(IMakeTheBestDecisionsForMyMostAbundantDreamLife['contentment'])

IMakeWonderfulDecisionsForMyselfThatAreSustainable = {'happy': 'creative', 'love': 'spending quality time with my children', 'bliss': 'healthy and happy', 'abundance': 'wealthy and rich'}
myDreamLifeILive = IMakeWonderfulDecisionsForMyselfThatAreSustainable['happy']
print(f"I am {myDreamLifeILive} !")
myDreamLifeIsAbundant = IMakeWonderfulDecisionsForMyselfThatAreSustainable['abundance']
print(f"I Am {myDreamLifeIsAbundant}!")

## Dictionaries can acquire New Key-Value Pairs  
# Dictionaries can change. They are dynamic.

# How to: name of dictionary, then put new key plus the new value, in square brackets

# x- and y-coordinates to display item.

angelChild = {'happy': 'smile', 'content': 'laughter'}
print(angelChild)

angelChild['x_coordinatePosition'] = 1
angelChild['y_coordinatePosition'] = 24
print(angelChild)

## Empty Dictionary, then Add Items or How To Fill An Empty Dictionary
# first, make a dictionary with braces
# second, put each key-value pair in
# each on its on line.

IAmSafe = {}

IAmSafe['GodProtectsMe'] = "It is certain that God Protects me and my children completely."
IAmSafe['GodLovesMe'] = "God's love for me and my children is unconditional."
    
print(IAmSafe)

# empty dictionaries are perfect for user-generated data, and also for code that automaticallycreates a lot of key-value pairs.

## changing values in a dictionary:
# first step: name of dictionary, with key in square brackets and assign new value to that key.

PhoenixMLStatus = {'rich': 'continuously very rich'}
print(f"Phoenix M L is {PhoenixMLStatus['rich']}.")

PhoenixMLStatus['rich'] = 'endlessly wealthy and growing richer'
print(f"Phoenix M L is now {PhoenixMLStatus['rich']}.")

## Track position of trajectory and upward growth of my riches!

PhoenixWealth = {'x_position': 0, 'y_position':100, 'daybydayGrowth': 'infiniteGrowthNow'}
print(f"First position: {PhoenixWealth['x_position']}")

# Move the position to the right
# Decide how far into the future to move Phoenix's Wealth based on the day by day growth.

if PhoenixWealth['daybydayGrowth'] == 'millionsOfTheMostValuableCurrency':
    x_bump = 1
elif PhoenixWealth['daybydayGrowth'] == 'infiniteGrowthNow':
    x_bump = 300

else:
    # This is an Abundant time, infinitely.
    x_bump = 2000

# The position is the original position plus the bump.
PhoenixWealth['x_position'] = PhoenixWealth['x_position'] + x_bump
print(f"New position: {PhoenixWealth['x_position']}")

# change one value in dictionary, to get overall characteristics of the dictionary.

PhoenixWealth['daybydayGrowth'] = 'whatDreamsAreMadeOf'
print(f"Phoenix M L is now {PhoenixWealth['daybydayGrowth']}.")

## Delete Key-Value Pairs in Dictionaries using del statement.

muffin = {'flavor': 'blueberries', 'nut-topping': 'pine nuts'}
print(muffin)

del muffin['nut-topping']
print(muffin)

## Similar objects in a dictionary.

favoriteHeartLanguage = {
    'touch': 'consensual touch',
    'soft lips': 'kisses on the forehead',
    'genuine': 'genuine heart',
    'honesty': 'honest compliments',
}

HeartLanguage = favoriteHeartLanguage['touch'].title()
print(f"My heart is full of love. {HeartLanguage} is okay.")


## Access Values with get()
# If key isn't in dictionary, an error occurs.

# totalBabe = {'gorgeousHair': 'shiny and full hair', 'pretty face': 'gorgeous features'}
# print(totalBabe['stars']) 
# stars isn't a key in the dictionary totalBabe, so it returns an error.

totalBabe = {'pretty hair': 'rainbow', 'pretty face': 'lovely face'}
starValue = totalBabe.get('stars', 'starValue is not in dictionary.')
print(starValue)
