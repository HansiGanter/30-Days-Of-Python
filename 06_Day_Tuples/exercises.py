import math

#####################
# Exercise: Level 1
#####################

# 1. Create an empty tuple
empty_tuple = ()

# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters = ("Veronika", "Carlota")
brothers = ("Enrique", "Kilian")

# 3. Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers

# 4. How many siblings do you have?
len(siblings)

# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = tuple(list(siblings) + ["Carmina", "Hans"])

#####################
# Exercise: Level 2
#####################

# 1. Unpack siblings and parents from family_members
siblings = family_members[:4]
parents = family_members[-2:]

# 2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ("banana", "orange", "mango", "lemon")
vegetables = ("Tomato", "Potato", "Cabbage", "Onion", "Carrot")
animal = ("dog", "cat", "fish", "chicken")
food_stuff_tp = fruits + vegetables + animal

# 3. Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

# 4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
if len(food_stuff_lt) % 2 == 0:
    middle = food_stuff_lt[
        (len(food_stuff_lt) // 2) - 1 : (len(food_stuff_lt) // 2) + 1
    ]
else:
    middle = food_stuff_lt[len(food_stuff_lt) // 2]

# 5. Slice out the first three items and the last three items from food_staff_lt list
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]

# 6. Delete the food_staff_tp tuple completely
del food_stuff_tp

# 7. Check if an item exists in tuple:
#   - Check if 'Estonia' is a nordic country
#   - Check if 'Iceland' is a nordic country
#   nordic_countries = ("Denmark", "Finland", "Iceland", "Norway", "Sweden")
nordic_countries = ("Denmark", "Finland", "Iceland", "Norway", "Sweden")
"Estonia" in nordic_countries
"Iceland" in nordic_countries
