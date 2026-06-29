# Organize a list

# sort() method: changes order of list permanently

# this example sorts it in alphabetical order permanently.

someofmlfirebirdtalentsalphabetical = [
    "knowing what to do for my highest good in every crucial moment",
    "receiving clarity immediately when important",
    "nurturing all important skills I need so that I am an expert at the important skill exactly when I need it",
]
someofmlfirebirdtalentsalphabetical.sort()
print(someofmlfirebirdtalentsalphabetical)

# reverse=True argument sorts the list in reverse-alphabetical order

someofmlfirebirdtalents = [
    "knowing what to do for my highest good in every crucial moment",
    "receiving clarity immediately at the best possible moment",
    "nurturing all important skills I need so that I am an expert at the important skill exactly when I need it",
]
someofmlfirebirdtalents.sort(reverse=True)
print(someofmlfirebirdtalents)

## sorted() function: sorts list temporarily
# it keeps the original order of list, while displaying in a particular sorted order.

mlfirebirdisreallygreatatthesethings = [
    "cooking beautiful, healthy meals",
    "living and experiencing her most amazing dream life",
    "taking really good care of herself, her life, and her growing wealth",
    "singing in her absolutely cool, gorgeous and beautiful style of singing that includes great singing technique and ever-improving, strong, natural, practiced, healthy, singing voice",
]

print("This is the original list:")
print(mlfirebirdisreallygreatatthesethings)

print("\nThis is the sorted list (in alphabetical order):")
print(sorted(mlfirebirdisreallygreatatthesethings))

print("\nWe display the original list again:")
print(mlfirebirdisreallygreatatthesethings)

# sorted() function includes being able to display a list reverse-alphabetically.
# note: sorting lists alphabetically are straightforward for lowercase.
# sorting specific lists with capital letters require more precise programming.

## reverse() method: reverse original order of the list
# reverse() does not sort alphabetically,
# only reverse chronologically of the original list permanently.
# however, you can restore to original order by using reverse() to the list again.

mlfirebirdisreallyfree = [
    "Phoenix is free.",
    "M.L. is free from all limitations.",
    "M.L. Phoenix is free to pursue all her dreams now.",
]
print(mlfirebirdisreallyfree)

mlfirebirdisreallyfree.reverse()

print(mlfirebirdisreallyfree)

## len() function: helps us find the length of a list.

mlfirebirdisattheveryleastaveryprotectedmultitrillionaireofthehighestavailablecurrencyatalltimes = [
    "14000000000000",
    "50000000000000",
    "200000000000000",
]
print(
    len(
        mlfirebirdisattheveryleastaveryprotectedmultitrillionaireofthehighestavailablecurrencyatalltimes
    )
)

## Avoid index errors when using lists.
# common errors: asking for 4th item when you only have 3 items.
# python tries to give you item at index 3.
# so it says IndexError: list is out of range.
# humans usually count from 1, however, Python counts from 0.
# solution, try adjusting the index by 1.
# another solution is that -1 index will always give you the last item.
# however, this can cause an error if you request the last item from an empty list:

flowers = []
print(flowers[-1])

# Python will say IndexError: list index out of range

## troubleshooting index error:
# - print your list
# - print length of list
