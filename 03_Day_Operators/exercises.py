import math

# 1. Declare your age as integer variable
age = 31

# 2. Declare your height as a float variable
height = 1.85

# 3. Declare a variable that store a complex number
complex_number = 1j

# 4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
#       Enter base: 20
#       Enter height: 10
#       The area of the triangle is 100
print(
    "The area of the triangle is",
    int(input("Enter base: ")) * int(input("Enter height: ")) / 2,
)

# 5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
#       Enter side a: 5
#       Enter side b: 4
#       Enter side c: 3
#       The perimeter of the triangle is 12
print(
    "The perimeter of the triangle is",
    int(input("Enter side a: "))
    + int(input("Enter side b: "))
    + int(input("Enter side c: ")),
)

# 6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = int(input("length: "))
width = int(input("width: "))
print("area is", length * width, "perimeter is", length + width)

# 7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radius = int(input("radius: "))
print("area is", math.pi * radius * radius, "circumference is", 2 * math.pi * radius)

# 8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
slope1 = 2
x_intercept = 2 / 2
y_intercept = 2 * 0 - 2

# 9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
slope2 = (10 - 2) / (6 - 2)
euc_dist = math.sqrt((6 - 2) ** 2 + (10 - 2) ** 2)

# 10. Compare the slopes in tasks 8 and 9.
slope1 == slope2

# 11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
x_when_y_0 = -3

# 12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
len("python") != len("dragon")

# 13. Use and operator to check if 'on' is found in both 'python' and 'dragon'
"on" in "python" and "on" in "dragon"

# 14. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
"jargon" in "I hope this course is not full of jargon."

# 15. There is no 'on' in both dragon and python
not ("on" in "dragon" and "on" in "python")

# 16. Find the length of the text python and convert the value to float and convert it to string
str(float(len("python")))

# 17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
number = 3
number % 2 == 0

# 18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
7 // 3 == int(2.7)

# 19. Check if type of '10' is equal to type of 10
type(10) == type("10")

# 20. Check if int('9.8') is equal to 10
10 == int(9.8)

# 21. Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
#       Enter hours: 40
#       Enter rate per hour: 28
#       Your weekly earning is 1120
print(
    "Your weekly earning is",
    int(input("Enter hours: ")) * int(input("Enter rate per hour: ")),
)

# 22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
#       Enter number of years you have lived: 100
#       You have lived for 3153600000 seconds.
print(
    "You have lived for",
    int(input("Enter number of years you have lived: ")) * 60 * 60 * 24 * 365,
    "seconds.",
)

# 23. Write a Python script that displays the following table
#       1 1 1 1 1
#       2 1 2 4 8
#       3 1 3 9 27
#       4 1 4 16 64
#       5 1 5 25 125
for i in [1, 2, 3, 4, 5]:
    print(i, 1, i, i**2, i**3)
