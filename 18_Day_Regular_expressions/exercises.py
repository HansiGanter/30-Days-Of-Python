#####################
# Exercise: Level 1
#####################

import re

# 1. What is the most frequent word in the following paragraph?
print("=======> Task 1")

paragraph = "I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love."


def most_frequent_word(paragraph):
    words = re.findall(r"\b\w+\b", paragraph)
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    return sorted(word_counts.items(), key=lambda x: x[1], reverse=True)


print(most_frequent_word(paragraph))

# [
#    (6, 'love'),
#    (5, 'you'),
#    (3, 'can'),
#    (2, 'what'),
#    (2, 'teaching'),
#    (2, 'not'),
#    (2, 'else'),
#    (2, 'do'),
#    (2, 'I'),
#    (1, 'which'),
#    (1, 'to'),
#    (1, 'the'),
#    (1, 'something'),
#    (1, 'if'),
#    (1, 'give'),
#    (1, 'develop'),
#    (1, 'capabilities'),
#    (1, 'application'),
#    (1, 'an'),
#    (1, 'all'),
#    (1, 'Python'),
#    (1, 'If')
# ]

# 2. The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.
print("=======> Task 2")


text = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles."

points = re.findall(r"-?\d+", text)
sorted_points = sorted(points, key=int)
distance = int(sorted_points[-1]) - int(sorted_points[0])
print(distance)

# points = ["-12", "-4", "-3", "-1", "0", "2", "4", "8"]
# sorted_points = [-12, -4, -3, -1, -1, 0, 2, 4, 8]
# distance = 8 - (-12)  # 20

#####################
# Exercise: Level 2
#####################

# 3. Write a pattern which identifies if a string is a valid python variable
print("=======> Task 3")


def is_valid_variable(variable):
    return re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", variable) is not None


print(is_valid_variable("first_name"))  # True
print(is_valid_variable("first-name"))  # False
print(is_valid_variable("1first_name"))  # False
print(is_valid_variable("firstname"))  # True

#####################
# Exercise: Level 3
#####################

# 4.Clean the following text. After cleaning, count three most frequent words in the string.
print("=======> Task 4")
sentence = """%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?"""


def clean_text(text):
    return re.sub(r"[^a-zA-Z0-9\s]", "", text)


# I am a teacher and I love teaching There is nothing as more rewarding as educating and empowering people I found teaching more interesting than any other jobs Does this motivate you to be a teacher


def most_frequent_words(text):
    words = re.findall(r"\b\w+\b", text)
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    return sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:7]


print(clean_text(sentence))
print(
    most_frequent_words(clean_text(sentence))
)  # [(3, 'I'), (2, 'teaching'), (2, 'teacher')]
