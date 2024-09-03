#####################
# Exercise: Level 1
#####################

# 1. Write a function which generates a six digit/character random_user_id.
print("=======> Task 1")

import random
import string


def random_user_id():
    return "".join(random.choices(string.ascii_letters + string.digits, k=6))


print(random_user_id())  # '1ee33d'

# 2. Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
print("=======> Task 2")


def user_id_gen_by_user():
    num_char = int(input("How many characters? "))
    num_ids = int(input("How many ids? "))
    return [
        "".join(random.choices(string.ascii_letters + string.digits, k=num_char))
        for x in range(num_ids)
    ]


print(user_id_gen_by_user())  # user input: 5 5
# output:
# kcsy2
# SMFYb
# bWmeq
# ZXOYh
# 2Rgxf

print(user_id_gen_by_user())  # 16 5
# 1GCSgPLMaBAVQZ26
# YD7eFwNQKNs7qXaT
# ycArC5yrRupyG00S
# UbGxOFI7UXSWAyKN
# dIV0SSUTgAdKwStr


# 3. Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
print("=======> Task 3")


def rgb_color_gen():
    return (
        f"rgb{(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))}"
    )


print(rgb_color_gen())

# rgb(125,244,255) - the output should be in this form

#####################
# Exercise: Level 2
#####################

# 4. Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
print("=======> Task 4")


def list_of_hexa_colors(number_hex):
    return [
        "#" + "".join(random.choices("0123456789abcdef", k=6))
        for _ in range(number_hex)
    ]


print(list_of_hexa_colors(3))

# 5. Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
print("=======> Task 5")


def list_of_rgb_colors(n):
    return [rgb_color_gen() for _ in range(n)]


print(list_of_rgb_colors(3))

# 6. Write a function generate_colors which can generate any number of hexa or rgb colors.
print("=======> Task 6")


def generate_colors(type, n):
    return (
        [rgb_color_gen() for _ in range(n)] if type == "rgb" else list_of_hexa_colors(n)
    )


print(generate_colors("hexa", 3))  # ['#a3e12f','#03ed55','#eb3d2b']
print(generate_colors("hexa", 1))  # ['#b334ef']
print(
    generate_colors("rgb", 3)
)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80']
print(generate_colors("rgb", 1))  # ['rgb(33,79, 176)']

#####################
# Exercise: Level 3
#####################

# 7. Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
print("=======> Task 7")


def shuffle_list(list):
    return random.sample(list, len(list))


print(shuffle_list([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# 8. Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
print("=======> Task 8")


def random_numbers():
    return random.sample(range(10), 7)


print(random_numbers())
