#####################
# Exercise: Level 1
#####################

# 1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
#   Enter your age: 30
#   You are old enough to learn to drive.
#   Output:
#   Enter your age: 15
#   You need 3 more years to learn to drive.
age = int(input("Enter your age: "))
(
    print("You are old enough to learn to drive.")
    if age >= 18
    else print(f"You need {18-age} more years to learn to drive.")
)


# 2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
#   Enter your age: 30
#   You are 5 years older than me.
my_age = int(input("Enter my age: "))
your_age = int(input("Enter your age: "))
age_diff = my_age - your_age

if age_diff == 0:
    print("same age")
elif age_diff > 0:
    print(f"I am {age_diff} {"years" if age_diff > 1 else "year"} older than you.")
else:
    age_diff *= -1
    print(f"You are {age_diff} {"years" if age_diff < 1 else "year"} older than me. ")

# 3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
#   Enter number one: 4
#   Enter number two: 3
#   4 is greater than 3
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))
if a > b:
    print("a is greater than b")
elif a < b:
    print("a is smaller than b")
else:
    print("a is equal to b")


#####################
# Exercise: Level 2
#####################

# 4. Write a code which gives grade to students according to theirs scores:
#   80-100, A
#   70-89, B
#   60-69, C
#   50-59, D
#   0-49, F
grade = int(input("grade: "))
if grade >= 80:
    print("A")
elif grade >= 70:
    print("B")
elif grade >= 60:
    print("C")
elif grade >= 50:
    print("D")
else:
    print("F")

# 5. Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
month = input("Month: ")
autumn, winter,spring,summer = ["September", "October","November"],["December", "January", "February"],["March", "April","May"],["June", "July" , "August"]

if(month in autumn):
    print("Autumn")
elif(month in winter):
    print("Winter")
elif(month in spring):
    print("Spring")
elif(month in summer):
    print("Summer")
else:
    print("No month entered")

# 6. The following list contains some fruits:
#   fruits = ['banana', 'orange', 'mango', 'lemon']
# - If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')

#####################
# Exercise: Level 3
#####################

# 7. Here we have a person dictionary. Feel free to modify it!
person = {
    "first_name": "Asabeneh",
    "last_name": "Yetayeh",
    "age": 250,
    "country": "Finland",
    "is_marred": True,
    "skills": ["JavaScript", "React", "Node", "MongoDB", "Python"],
    "address": {"street": "Space street", "zipcode": "02210"},
}

# - Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
print(person["skills"][int(len(person["skills"])/2)]) if "skills" in person.keys() else print("no skills")

# - Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
print("Python" in person["skills"]) if "skills" in person.keys() else print("no skills")

# - If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
if len(person["skills"]) > 2 and set(["JavaScript","React"]).issubset(set(person["skills"])):
    print('He is a front end developer')
elif len(person["skills"]) == 3 and set(["Node", "Python", "MongoDB"]).issubset(set(person["skills"])):
    print('He is a backend developer')
elif len(person["skills"]) == 3 and set(["React", "Node" , "MongoDB"]).issubset(set(person["skills"])):
    print('He is a fullstack developer')
else:
    print('unknown title')

# - If the person is married and if he lives in Finland, print the information in the following format:
#   Asabeneh Yetayeh lives in Finland. He is married.
print(f"{person["first_name"]} {person["last_name"]} lives in {person['country']}. He is {"married" if person['is_marred'] else "not married"}.")

