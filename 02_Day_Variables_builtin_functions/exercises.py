#####################
# Exercise: Level 1
#####################

# 1. Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py

# 2. Write a python comment saying 'Day 2: 30 Days of python programming'
# Day 2: 30 Days of python programming

# 3. Declare a first name variable and assign a value to it
first_name = "Hansi"

# 4. Declare a last name variable and assign a value to it
last_name = "Ganter"

# 5. Declare a full name variable and assign a value to it
full_name = first_name + " " + last_name

# 6. Declare a country variable and assign a value to it
country = "Austria"

# 7. Declare a city variable and assign a value to it
city = "Gmuend"

# 8. Declare an age variable and assign a value to it
age = 31

# 9. Declare a year variable and assign a value to it
year1 = 1993

# 10. Declare a variable is_married and assign a value to it
is_married = False

# 11. Declare a variable is_true and assign a value to it
is_true = False

# 12. Declare a variable is_light_on and assign a value to it
is_light_on = False

# 13. Declare multiple variable on one line
day, month, year = 15, 3, 1993

#####################
# Exercise: Level 2
#####################

# 1. Check the data type of all your variables using type() built-in function
type(first_name)
type(last_name)
type(full_name)
type(country)
type(city)
type(age)
type(year1)
type(is_married)
type(is_true)
type(is_light_on)
type(day)
type(month)
type(year)

# 2. Using the len() built-in function, find the length of your first name
len(first_name)

# 3. Compare the length of your first name and your last name
len_diff = len(first_name) - len(last_name)

# 4. Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4
#   i. Add num_one and num_two and assign the value to a variable total
total = num_one + num_two
#   ii. Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two
#   iii. Multiply num_two and num_one and assign the value to a variable product
product = num_two * num_one
#   iv. Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two
#   v. Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one
#   vi. Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one**num_two
#   vii. Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two

# 5. The radius of a circle is 30 meters.
import math

radius = 30
#   i. Calculate the area of a circle and assign the value to a variable name of area_of_circle
area_of_circle = math.pi * radius**2
#   ii. Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 2 * math.pi + radius
#   iii. Take radius as user input and calculate the area.
user_radius = int(input("Radius: "))
user_area = math.pi * user_radius**2

# 6. Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
user_first_name = input("user_first_name :")
user_last_name = input("user_last_name :")
user_country = input("user_country :")
user_age = int(input("user_age :"))

# 7. Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
help("keywords")
