# 1. Create an empty dictionary called dog
empty_dict = dict()

# 2. Add name, color, breed, legs, age to the dog dictionary
dog = {"name": "Bello", "color": "braun", "breed": "Bulldog", "legs": 4, "age": 7}

# 3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
students = {
    "first_name": "Hans",
    "last_name": "Ganter",
    "gender": "male",
    "age": 31,
    "marital_status": "single",
    "skills": ["programming", "basketball"],
    "country": "Austria",
    "city": "Gmünd",
    "address": "Schlossgasse 9",
}

# 4. Get the length of the student dictionary
print(len(students))

# 5. Get the value of skills and check the data type, it should be a list
print(type(students["skills"]))

# 6. Modify the skills values by adding one or two skills
students["skills"] += ["python", "JavaScript"]
print(students)

# 7. Get the dictionary keys as a list
print(students.keys())

# 8. Get the dictionary values as a list
print(students.values())

# 9. Change the dictionary to a list of tuples using items() method
print(students.items())

# 10. Delete one of the items in the dictionary
del students["marital_status"]
print(students)

# 11. Delete one of the dictionaries
del dog
