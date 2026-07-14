agentName = {
    'schoolName': 'Cassandra Love',
    'firstName': 'Cassandra',
    'lastName': 'Love',
    'tylerSchoolName': 'Tyler Durden',
    'tylerFirstName': 'Tyler',
    'tylerLastName': 'Durden',
    }

# any info in agentName can be retrieved, however, we can see everything at once, using the for loop.

for typeOfName, nameValue in agentName.items():
    print(f"\nType of Name: {typeOfName}")
    print(f"Name of Value: {nameValue}")

techSkillsAndDreamLifeSkills = {
    'Phoenix (really Great At Python)': 'python',
    'Phoenix (reallyGreatAtMath)': 'linear algebra',
    'Phoenix (reallyGreatAtCalculus)': 'calculus',
    'Phoenix (reallyGreatAtCodingWithR)': 'r',
    'Phoenix (reallyGreatAtCodingUsefulAndEthicalAI)': 'AI',
    'Phoenix (reallyGreatAtMakingMoneyAndBuildingWealth)': 'money and wealth',
    'Phoenix (reallyGreatAtCreatingFinancialFreedomAndWealthForMyselfandMyDreamLife)': 'financial freedom and wealth, and creating my dream life.'
    }

for skillsIAmGreatAt, nameOfMySkillsIAmFluentIn in techSkillsAndDreamLifeSkills.items():
    print(f"{skillsIAmGreatAt.title()} is fluent in {nameOfMySkillsIAmFluentIn.title()}.")

## How to loop through all keys in a dictionary:
# keys() method is for when you don't need to pull all the values in a dictionary.

fluentSkills = {
    'phoenix (python)': 'python',
    'phoenix (r)': 'r',
    'phoenix (acquiring everything and every skill, most useful for succeeding in her career and life, all in alignment with her highest self)': 'parent, taking great care of herself',
}

for phoenixSkills in fluentSkills.keys():
    print(phoenixSkills.title())

# if we remove keys(), it still has the same result as above:

for phoenixSkills in fluentSkills:
    print(phoenixSkills.title())


fluentSkills = {
    'phoenix (python)': 'python',
    'phoenix (r)': 'r',
    'phoenix (acquiring everything and every skill, most useful for succeeding in her career and life, all in alignment with her highest self)': 'parent, taking great care of herself',
}

phoenixHasQualifications = ['phoenix (python)', 'phoenix (r)']
for phoenixSkills in fluentSkills.keys():
    print(f"Hi {phoenixSkills.title()}.")

    skillQualifications = fluentSkills[phoenixSkills].title()
    print(f"\t{phoenixSkills.title()}, I see you are skilled and qualified in {skillQualifications}!")

## see if there is a new skill Phoenix wants to learn for fun and happiness

newSkill = {
    'phoenix (kickflip)': 'do a kickflip',
    'phoenix (colorgrading)': 'colorgrade',
}

if 'phoenix (surf)' not in newSkill.keys():
    print('Phoenix, you can practice surfing!')

## sorted() function helps you organize a loop in a particular order:

newSkill = {
    'Phoenix (kind)': 'practices kindness consistently when appropriate and safe',
    'Phoenix (loving)': 'practices loving care to herself',
    'Phoenix (good communicator)': 'practices great communication',
    }

for phoenixName in sorted(newSkill.keys()):
    print(f"{phoenixName.title()}, thank you for all your hard work, learning these skills in order to be fluent in them!")

## Loop through every value in a dictionary 
# Using values() method to get values without the keys.

favPastime = {
    'W': 'building sandcastles with Mom',
    'M': 'building sandcastles with W',
    }

print("Our favorite pastimes are listed:")
for ourFavPastime in favPastime.values():
    print(ourFavPastime.title())

## set() will omit duplicate values, and build a set based on unique values.

favActivities = {
    'W': 'Building Sandcastles with M',
    'M': 'Building Sandcastles with W and E',
    'E': 'Building Sandcastles with M',
}

print("This is a list of our favorite activities:")
for ourFavActivities in set(favActivities.values()):
    print(ourFavActivities.title())

# sets are not dictionaries, 
# they are both in braces
# but sets have no key-value pairs.
# sets do not have a specific order.
# lists and dictionaries can have a specific order.

