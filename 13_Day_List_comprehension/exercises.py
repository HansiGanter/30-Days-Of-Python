# 1. Filter only negative and zero in the list using list comprehension
print("=======> Task 1")

from pyparsing import java_style_comment


numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

print([i for i in numbers if i <= 0])


# 2. Flatten the following list of lists of lists to a one dimensional list :
print("=======> Task 2")

list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
print([number for row1 in list_of_lists for row in row1 for number in row])

# output
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 3. Using list comprehension create the following list of tuples:
print("=======> Task 3")

print([(i, 1, *[i**j for j in range(6)]) for i in range(11)])

# [(0, 1, 0, 0, 0, 0, 0),
# (1, 1, 1, 1, 1, 1, 1),
# (2, 1, 2, 4, 8, 16, 32),
# (3, 1, 3, 9, 27, 81, 243),
# (4, 1, 4, 16, 64, 256, 1024),
# (5, 1, 5, 25, 125, 625, 3125),
# (6, 1, 6, 36, 216, 1296, 7776),
# (7, 1, 7, 49, 343, 2401, 16807),
# (8, 1, 8, 64, 512, 4096, 32768),
# (9, 1, 9, 81, 729, 6561, 59049),
# (10, 1, 10, 100, 1000, 10000, 100000)]

# 4. Flatten the following list to a new list:
print("=======> Task 4")

countries = [[("Finland", "Helsinki")], [("Sweden", "Stockholm")], [("Norway", "Oslo")]]
print(
    [
        [c[0].upper(), c[0].upper()[:3], c[1].upper()]
        for country in countries
        for c in country
    ]
)
# output:
# [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]

# 5. Change the following list to a list of dictionaries:
print("=======> Task 5")

countries = [[("Finland", "Helsinki")], [("Sweden", "Stockholm")], [("Norway", "Oslo")]]

print(
    [
        {"country": c[0].upper(), "city": c[1].upper()}
        for country in countries
        for c in country
    ]
)
# output:
# [{'country': 'FINLAND', 'city': 'HELSINKI'},
# {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
# {'country': 'NORWAY', 'city': 'OSLO'}]

# 6. Change the following list of lists to a list of concatenated strings:
print("=======> Task 6")

names = [
    [("Asabeneh", "Yetayeh")],
    [("David", "Smith")],
    [("Donald", "Trump")],
    [("Bill", "Gates")],
]

print([f"{n[0]} {n[1]}" for name in names for n in name])

# output
# ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']

# 7. Write a lambda function which can solve a slope or y-intercept of linear functions.
print("=======> Task 7")

slope_and_intercept = lambda x1, y1, x2, y2: (
    (y2 - y1) / (x2 - x1),  # slope
    y1 - ((y2 - y1) / (x2 - x1)) * x1,  # y-intercept
)

# Example usage
x1, y1 = 1, 2
x2, y2 = 3, 4
m, b = slope_and_intercept(x1, y1, x2, y2)
print(f"Slope: {m}, Y-intercept: {b}")
