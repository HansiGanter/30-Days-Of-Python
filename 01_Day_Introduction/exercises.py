#####################
# Exercise: Level 2
#####################

# 1. Check the python version you are using
# =========================================
import sys

print(sys.version)

# 2. Open the python interactive shell and do the following operations. The operands are 3 and 4.
# ===============================================================================================

# addition(+)
print(3 + 4)
# subtraction(-)
print(3 - 4)
# multiplication(*)
print(3 * 4)
# modulus(%)
print(3 % 4)
# division(/)
print(3 / 4)
# exponential(**)
print(3**4)
# floor division operator(//)
print(3 // 4)

# 3 Write strings on the python interactive shell. The strings are the following:
# ===============================================================================

# Your name
print("Your name")
# Your family name
print("Your family name")
# Your country
print("Your country")
# I am enjoying 30 days of python
print("I am enjoying 30 days of python")

# 4 Check the data types of the following data:
# ===============================================

# 10
print(type(10))
# 9.8
print(type(9.8))
# 3.14
print(type(3.14))
# 4 - 4j
print(type(4 - 4j))
# ['Asabeneh', 'Python', 'Finland']
print(type(["Asabeneh", "Python", "Finland"]))
# Your name
print(type("Your name"))
# Your family name
print(type("Your family name"))
# Your country
print(type("Your country"))

#####################
# Exercise: Level 3
#####################

# 1. Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.
# ==============================================================================================================================================

print(1)
print(1.0)
print(1j)
print("1")
print(False)
print([1, 2, 3])
print((1, 2, 3))
print({1, 2, 3})
print({"one": 1, "two": 2, "three": 3})

# 2. Find an Euclidian distance between (2, 3) and (10, 8)
# ========================================================
import math

print((math.sqrt((10 - 2) ** 2 + (8 - 3) ** 2)))
