## Combine lists and if statements
# there may be special values that need a different treatment than other values in the list.
# you can organize changing conditions

## Check if value is special

iceCreamToppings = ['nuts', 'candy', 'sprinkles']

for iceCreamTopping in iceCreamToppings:
    print(f"Sprinkling {iceCreamTopping}.")

print("\nYour ice cream is all topped off!")

## Check if value is in list before adding it to the list.

potentialIceCreamToppings = ['stevia', 'coconut hardshell', 'turtle chocolate']

for potentialIceCreamTopping in potentialIceCreamToppings:
    if potentialIceCreamTopping == 'coconut hardshell':
        print("We are in the process of dreaming up coconut hardshell.")
    else:
        print(f"Sprinkling {potentialIceCreamTopping}.")
print("\nYour ice cream is ready!")

## Check if list is empty before a for loop.
# if conditional test fails, we ask if they are okay with just vanilla ice cream with not sprinkles.

potentialIceCreamToppings = []

if potentialIceCreamToppings:
    for potentialIceCreamTopping in potentialIceCreamToppings:
        print(f"Sprinkling {potentialIceCreamTopping}.")
    print("\nYour Ice Cream is ready!")
else:
    print("Are you okay with Vanilla? Do you like vanilla ice cream?")

## Using Multiple Lists

# check if a list is empty before executing a for loop.
potentialIceCreamToppings = []

if potentialIceCreamToppings:
    for potentialIceCreamTopping in potentialIceCreamToppings:
        print(f"Sprinkling {potentialIceCreamTopping}.")
    print("\nYour Ice Cream is ready!")
else:
    print("Do you want vanilla ice cream?")

## Checking That a List Is Not Empty

iceCreamToppings = []
for iceCreamTopping in iceCreamToppings:
    print(f"Sprinkling {iceCreamTopping}.")
    print("\nYour ice cream is ready!")
else:
    print("Would you like vanilla ice cream with no toppings?")

# if the list is not empty, the ice cream topping you chose will be added to the ice cream cone!

## Multiple Lists:

toppingsWeHave = ['sprinkles', 'chocolate chips', 'hazelnut', 
                  'almond slices', 'pine nuts', 'croissant bits']

customerWantsToppings = ['unicorn pimples', 'unicorn hair', 'unicorn whimsy']

for customerWantsToppings in toppingsWeHave:
    if customerWantsToppings in toppingsWeHave:
        print(f"Sprinkling {customerWantsToppings}.")
    else:
        print(f"Sorry, {customerWantsToppings} is not available.")
print("\nIceCream is ready!")

## style of If Statements

# if amountOfMoney < 3:
# is preferred over
# if amountOfMoney<3:

# python still reads it the same despite the spacing differences,
# however, it's more legible for humans who read the code!!! I love Humans.





    
