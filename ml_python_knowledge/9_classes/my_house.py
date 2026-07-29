from house import House
from dream_house import DreamHouse

my_dream_house = House('luscious', 'tall & modern', 'water & mountains')
print(my_dream_house.get_descriptive_name())

my_dream_house.read_available_to_buy = 91000000
my_dream_house.display_money_available()

## Import entire module example:
# after importing, we access the classes via module_example.ClassExample syntax.
# import house
# my_river_house = house.House('riverbrook', 'architectural gem', 'river trees mountains birds')
# print(my_river_house.get_descriptive_name())

# my_beach_mountain_house = house.DreamHouse('beach', 'modern beautiful architectural gem', 'ocean view')
# print(my_beach_mountain_house.get_descriptive_name())
