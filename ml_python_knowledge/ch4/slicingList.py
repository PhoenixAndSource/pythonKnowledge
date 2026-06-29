## Slice List

dreamLife = [
    "happy",
    "secure",
    "loved",
    "peace",
    "treated with kindness and respect",
    "safe",
    "happiness in my heart and reflected all around me",
]
print(dreamLife[0:4])
print(dreamLife[0:])
print(dreamLife[1:])
print(dreamLife[-2:])

## Looping Through A slice

healthyfoodsthatsupportmeandmybeautyaesthetic = [
    "strawberries",
    "blueberries",
    "avocados",
    "carrots",
    "persimmon",
    "lentils",
    "seitan",
    "natural, sugar-free soy-based ice cream",
    "pomegranate",
]
for examplesofhealthyfoodsienjoy in healthyfoodsthatsupportmeandmybeautyaesthetic[:3]:
    print(examplesofhealthyfoodsienjoy.title())

## Copying a List

my_healthy_foods = [
    "papaya",
    "pineapple",
    "mango",
    "fresh young coconut",
    "avocado",
    "carrot",
]
my_favorite_foods = my_healthy_foods[:]

print("My healthy foods that happen to be my favorite foods are:")
print(my_healthy_foods)

print("\nMy favorite foods that happen to be healthy foods are:")
print(my_favorite_foods)

# to show that we have two separate lists, we'll add a new food to the healthy food list, and the favorite food list.

my_healthy_foods.append("watermelon")
my_favorite_foods.append("hood strawberries")

print("My healthy foods that happen to be my favorite foods are:")
print(my_healthy_foods)

print("My favorite foods that happen to be healthy foods are:")
print(my_favorite_foods)
