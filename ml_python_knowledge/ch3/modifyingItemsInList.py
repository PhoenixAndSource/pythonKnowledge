# usually you build a list, then add or remove items as program progresses through.

# ML's example:
# storing membership names in a list,
# then removing names as membership declines,
# adding names as members join.

mltopracticeskills = ["guitar", "bass guitar", "piano", "singing"]
print(mltopracticeskills)

# change first item [0] 'guitar' to '5-string guitar'

mltopracticeskills[0] = "5-string guitar"
print(mltopracticeskills)

# Adding items to a list
# one way to add items to a list is to append the item to the list.
# here is how to add 'driving a motorcycle' to the end of the list.

mltopracticeskills = ["guitar", "bass guitar", "piano", "singing"]
print(mltopracticeskills)

mltopracticeskills.append("driving a motorcycle")
print(mltopracticeskills)

# the append() method helps you build lists dynamically.
# here is how to start with an empty list.
# calling in my kids and loved ones

mltopracticeskills = []
mltopracticeskills.append("guitar")
mltopracticeskills.append("singing")
mltopracticeskills.append(
    "making a lot of money in a way that is for my highest good, which benefits me with harm to none, and is the opposite of self-sabotabge."
)
mltopracticeskills.append("getting my kids back to live with me legally.")
mltopracticeskills.append(
    "getting my family back loving me and supporting me in a genuine way"
)
mltopracticeskills.append("the opposite of self-sabotage")

print(mltopracticeskills)

# insert items into a list
# put items in deliberate specific order with the insert() method
# instructions: state index of new item, and value of new item.

mltopracticeskillsimmediatelyandcompletelyandsuccessfullyformlhighestgood = [
    "playing guitar",
    "getting my kids back",
    "living in balance",
    "taking good care of myself",
]

mltopracticeskillsimmediatelyandcompletelyandsuccessfullyformlhighestgood.insert(
    0,
    "making a large, comfortable amount of money for myself that benefits me tremendously",
)
mltopracticeskillsimmediatelyandcompletelyandsuccessfullyformlhighestgood.insert(
    2, "excelling at doing the opposite of self-sabotage"
)
print(mltopracticeskillsimmediatelyandcompletelyandsuccessfullyformlhighestgood)

# removing an item or set of items from a list
# Example: if you've already practiced skill: you may want to remove the item from the list

# remove item with del statement, if you know the index of item.

theskillsIpracticeeverydayformyhighestgoodwhilecheckingoffalreadysuccessfulitemsbydeletingfromthislist = [
    "practice guitar",
    "taken good care of my spirit",
    "make more than enough money and be able to hold more than enough money to thrive and to be comfortable and safe",
    "do the opposite of self-sabotage to my benefit with harm to none",
]

del theskillsIpracticeeverydayformyhighestgoodwhilecheckingoffalreadysuccessfulitemsbydeletingfromthislist[
    1
]
print(
    theskillsIpracticeeverydayformyhighestgoodwhilecheckingoffalreadysuccessfulitemsbydeletingfromthislist
)

# removing item with pop() method
# useful for if you need value of item after it has been removed from list
# it removes the last item in a list, but allows you to use it after removing it.
# example: remove item already done, add it to different list of done items.

mlpracticeskills = ["being in a high vibration", "work out abs", "do pushups"]
print(mlpracticeskills)

popped_mlpracticeskills = mlpracticeskills.pop()
print(mlpracticeskills)
print(popped_mlpracticeskills)

# example of when pop() method can be useful
# if items on list are stored in chronological order
# and we want to recall the most recent skill we acquired.

recent_skills_practiced_with_success_by_ml = [
    "my ability to own and enjoy my dream cars that work flawlessly and are maintained properly throughout its lifecycle for my highest good",
    "my ability to transmute all energies that come into my field, instantly, into abundance, good health, good spirit, prosperity, financial wealth, love, success and happiness for my highest good, with harm to none",
    "my ability to have all bills (including any dream car payments owned by me, ML) paid on time and paid off without self-sabotage, for my highest good",
]

recent_skills_acquired_with_success_by_ml = (
    recent_skills_practiced_with_success_by_ml.pop()
)
print(
    f"The most recent skill I successfully acquired is {recent_skills_acquired_with_success_by_ml}."
)

# pop items from any index on list by
# including the index of item to be removed in parentheses:

recent_skills_acquired_with_success_by_ml = [
    "my ability to own, enjoy, and have my dream cars paid off in full without self-sabotage, for my highest good",
    "my ability to own and have my dream houses paid off in full without self-sabotage, for my highest good",
    "my ability to have permanent, financial freedom, financial wealth, financial prosperity and financial stability for my highest good, while never self-sabotaging, with harm to none.",
    "my ability to have permanent good health, prosperity, wealth, love and freedom with no self-sabotage, all for my highest good with harm to none.",
]

print(recent_skills_acquired_with_success_by_ml)

mlisalreadylivingthisdreamlife = "my ability to own and have my dream houses paid off in full without self-sabotage, for my highest good"
recent_skills_acquired_with_success_by_ml.remove(mlisalreadylivingthisdreamlife)
print(recent_skills_acquired_with_success_by_ml)
print(
    f"\nI have already acquired {mlisalreadylivingthisdreamlife.title()}, hence I am enjoying living the result of this skill acquired at the present moment."
)

mlisalreadylivingthisdreamlifereality1 = "my ability to own, enjoy, and have my dream cars paid off in full without self-sabotage, for my highest good"
recent_skills_acquired_with_success_by_ml.remove(mlisalreadylivingthisdreamlifereality1)
print(recent_skills_acquired_with_success_by_ml)
print(
    f"\nI have, also, already acquired {mlisalreadylivingthisdreamlifereality1}, hence I, M.L., am enjoying living the result of this skill acquired at the present moment."
)
