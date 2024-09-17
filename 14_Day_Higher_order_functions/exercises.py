from functools import reduce
from turtle import up


countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland"]
names = ["Asabeneh", "Lidiya", "Ermias", "Abraham"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#####################
# Exercise: Level 1
#####################

# 1. Explain the difference between map, filter, and reduce.
print("=======> Task 1")

print(
    "Map: Make an iterator that computes the function using arguments from each of the iterables. Stops when the shortest iterable is exhausted."
)
print(
    "Filter: Return an iterator yielding those items of iterable for which function(item) is true. If function is None, return the items that are true."
)
print(
    "Reduce: Apply a function of two arguments cumulatively to the items of a sequence or iterable, from left to right, so as to reduce the iterable to a single value. For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5). If initial is present, it is placed before the items of the iterable in the calculation, and serves as a default when the iterable is empty."
)
# 2. Explain the difference between higher order function, closure and decorator
print("=======> Task 2")

print(
    "Higher order function: A function that takes another function as an argument and returns a new function."
)
print(
    "Closure: A function that remembers and has access to its outer scope variables even after the outer function has returned."
)
print(
    "Decorator: A function that takes another function and extends its functionality without explicitly modifying it. Decorators are usually called before the function they decorate. They are used to add new functionality to an existing function."
)

# 3. Define a call function before map, filter or reduce, see examples.
print("=======> Task 3")


def call(func):
    return func()


# 4. Use for loop to print each country in the countries list.
print("=======> Task 4")

for country in countries:
    print(country)

# 5. Use for to print each name in the names list.
print("=======> Task 5")

for name in names:
    print(name)

# 6. Use for to print each number in the numbers list.
print("=======> Task 6")

for number in numbers:
    print(number)

#####################
# Exercise: Level 2
#####################

# 7. Use map to create a new list by changing each country to uppercase in the countries list
print("=======> Task 7")

print(list(map(lambda x: x.upper(), countries)))

# 8. Use map to create a new list by changing each number to its square in the numbers list
print("=======> Task 8")

print(list(map(lambda x: x * x, numbers)))

# 9. Use map to change each name to uppercase in the names list
print("=======> Task 9")

print(list(map(lambda x: x.upper(), names)))

# 10. Use filter to filter out countries containing 'land'.
print("=======> Task 10")

print(list(filter(lambda x: "land" not in x, countries)))

# 11. Use filter to filter out countries having exactly six characters.
print("=======> Task 11")

print(list(filter(lambda x: len(x) == 6, countries)))

# 12. Use filter to filter out countries containing six letters and more in the country list.
print("=======> Task 12")

print(list(filter(lambda x: len(x) >= 6, countries)))

# 13. Use filter to filter out countries starting with an 'E'
print("=======> Task 13")

print(list(filter(lambda x: not x.startswith("E"), countries)))

# 14. Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
print("=======> Task 14")

print(
    list(
        map(
            lambda x: x.upper(),
            filter(lambda x: len(x) >= 6, countries),
        )
    )
)

# 15. Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
print("=======> Task 15")


def get_string_lists(lst):
    return list(map(lambda x: str(x), lst))


print(get_string_lists([1, "a", "b", 2, "c", 3]))

# 16. Use reduce to sum all the numbers in the numbers list.
print("=======> Task 16")

print(reduce(lambda x, y: x + y, numbers))

# 17. Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
print("=======> Task 17")

print(
    reduce(
        lambda x, y: x + ", " + y,
        countries,
    ),
    " are north European countries",
)

# 18. Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js (eg 'land', 'ia', 'island', 'stan')).
print("=======> Task 18")

import sys
import os

# Add the parent directory to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

# Now import the countries
from data.countries import countries


def categorize_countries(pattern):
    return list(filter(lambda x: pattern.lower() in x.lower(), countries))


# Test the function with different patterns
print("Countries with 'land':", categorize_countries("land"))
print("Countries with 'ia':", categorize_countries("ia"))
print("Countries with 'island':", categorize_countries("island"))
print("Countries with 'stan':", categorize_countries("stan"))

# 19. Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
print("=======> Task 19")


def count_countries_by_letter(countries):
    return {
        letter: len(list(filter(lambda x: x.startswith(letter), countries)))
        for letter in set(map(lambda x: x[0], countries))
    }


print(count_countries_by_letter(countries))

# 20. Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
print("=======> Task 20")


def get_first_ten_countries(countries):
    return countries[:10]


print(get_first_ten_countries(countries))

# 21. Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
print("=======> Task 21")


def get_last_ten_countries(countries):
    return countries[-10:]


print(get_last_ten_countries(countries))


#####################
# Exercise: Level 3
#####################

# 22. Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:
# - Sort countries by name, by capital, by population
print("=======> Task 22")

import data.countries_data as countries_data

print(sorted(countries_data.data, key=lambda x: x["name"]))
print(sorted(countries_data.data, key=lambda x: x["capital"]))
print(sorted(countries_data.data, key=lambda x: x["population"]))

# - Sort out the ten most spoken languages by location.
print("=======> Sort out the ten most spoken languages by location.")

print(sorted(countries_data.data, key=lambda x: x["languages"])[:10])

# - Sort out the ten most populated countries.
print("=======> Sort out the ten most populated countries.")

print(sorted(countries_data.data, key=lambda x: x["population"])[:10])
