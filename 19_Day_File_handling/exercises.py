#####################
# Exercise: Level 1
#####################

# 1. Write a function which count number of lines and number of words in a text. All the files are in the data the folder: a) Read obama_speech.txt file and count number of lines and words b) Read michelle_obama_speech.txt file and count number of lines and words c) Read donald_speech.txt file and count number of lines and words d) Read melina_trump_speech.txt file and count number of lines and words
print("=======> Task 1")


def count_lines_words(filename):
    with open(filename) as file:
        text = file.read()
        lines = text.split("\n")
        words = text.split()
        return len(lines), len(words)


print(count_lines_words("./data/obama_speech.txt"))
print(count_lines_words("./data/michelle_obama_speech.txt"))
print(count_lines_words("./data/donald_speech.txt"))
print(count_lines_words("./data/melina_trump_speech.txt"))

# 2. Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages
print("=======> Task 2")

import json


def most_spoken_languages(filename, n):
    with open(filename) as file:
        data = json.load(file)
        languages = {}
        for country in data:
            for language in country["languages"]:
                languages[language] = languages.get(language, 0) + 1
        return sorted(languages.items(), key=lambda x: x[1], reverse=True)[:n]


# Your output should look like this
print(most_spoken_languages(filename="./data/countries_data.json", n=10))
# [(91, 'English'), (45, 'French'), (25, 'Arabic'), (24, 'Spanish'), (9, 'Russian'), (9, 'Portuguese'), (8, 'Dutch'), (7, 'German'), (5, 'Chinese'), (4, 'Swahili'), (4, 'Serbian')]

# Your output should look like this
print(most_spoken_languages(filename="./data/countries_data.json", n=3))
# [(91, 'English'), (45, 'French'), (25, 'Arabic')]

# 3. Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries
print("=======> Task 3")


def most_populated_countries(filename, n):
    with open(filename) as file:
        data = json.load(file)
        countries = sorted(data, key=lambda x: x["population"], reverse=True)[:n]
        return list(
            map(
                lambda country: {
                    "country": country["name"],
                    "population": country["population"],
                },
                countries,
            )
        )[:n]


# Your output should look like this
print(most_populated_countries(filename="./data/countries_data.json", n=10))
# [ {'country': 'China', 'population': 1377422166}, {'country': 'India', 'population': 1295210000}, {'country': 'United States of America', 'population': 323947000}, {'country': 'Indonesia', 'population': 258705000}, {'country': 'Brazil', 'population': 206135893}, {'country': 'Pakistan', 'population': 194125062}, {'country': 'Nigeria', 'population': 186988000}, {'country': 'Bangladesh', 'population': 161006790}, {'country': 'Russian Federation', 'population': 146599183}, {'country': 'Japan', 'population': 126960000} ]

# Your output should look like this
print(most_populated_countries(filename="./data/countries_data.json", n=3))
# [ {'country': 'China', 'population': 1377422166}, {'country': 'India', 'population': 1295210000}, {'country': 'United States of America', 'population': 323947000} ]

#####################
# Exercise: Level 2
#####################

# 4. Extract all incoming email addresses as a list from the email_exchange_big.txt file.
print("=======> Task 4")


def extract_emails(filename):
    incoming_emails = set()

    with open(filename) as file:
        for line in file:
            if line.startswith("From:"):
                email = line.split(": ")[1].strip()
                incoming_emails.add(email)

    return list(incoming_emails)


print(extract_emails("./data/email_exchanges_big.txt"))

# 5. Find the most common words in the English language. Call the name of your function find_most_common_words, it will take two parameters - a string or a file and a positive integer, indicating the number of words. Your function will return an array of tuples in descending order. Check the output
# Your output should look like this
print("=======> Task 5")


def find_most_common_words(filename, n):
    with open(filename) as file:
        text = file.read()
        words = text.split()
        word_counts = {}
        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1
        return sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:n]


# Your output should look like this
print(find_most_common_words("./data/obama_speech.txt", 10))
# [(10, 'the'), (8, 'be'), (6, 'to'), (6, 'of'), (5, 'and'), (4, 'a'), (4, 'in'), (3, 'that'), (2, 'have'), (2, 'I')]

# Your output should look like this
print(find_most_common_words("./data/obama_speech.txt", 5))
# [(10, 'the'), (8, 'be'), (6, 'to'), (6, 'of'), (5, 'and')]

# 6. Use the function, find_most_common_words to find: a) The ten most frequent words used in Obama's speech b) The ten most frequent words used in Michelle's speech c) The ten most frequent words used in Trump's speech d) The ten most frequent words used in Melina's speech
print("=======> Task 6")

print(find_most_common_words("./data/obama_speech.txt", 10))
print(find_most_common_words("./data/michelle_obama_speech.txt", 10))
print(find_most_common_words("./data/donald_speech.txt", 10))
print(find_most_common_words("./data/melina_trump_speech.txt", 10))

# 7. Write a python application that checks similarity between two texts. It takes a file or a string as a parameter and it will evaluate the similarity of the two texts. For instance check the similarity between the transcripts of Michelle's and Melina's speech. You may need a couple of functions, function to clean the text(clean_text), function to remove support words(remove_support_words) and finally to check the similarity(check_text_similarity). List of stop words are in the data directory
print("=======> Task 7")


def clean_text(text):
    return (
        text.lower().replace(".", "").replace(",", "").replace("!", "").replace("?", "")
    )


def remove_support_words(text):
    with open("./data/stop_words.py") as file:
        stop_words = file.read().split()
        return [word for word in text if word not in stop_words]


def check_text_similarity(text1, text2):
    cleaned_text1 = clean_text(text1)
    cleaned_text2 = clean_text(text2)
    words1 = remove_support_words(cleaned_text1)
    words2 = remove_support_words(cleaned_text2)
    return len(set(words1) & set(words2)) / len(set(words1) | set(words2))


print(
    check_text_similarity("./data/obama_speech.txt", "./data/michelle_obama_speech.txt")
)
print(check_text_similarity("./data/obama_speech.txt", "./data/donald_speech.txt"))
print(
    check_text_similarity("./data/obama_speech.txt", "./data/melina_trump_speech.txt")
)

# 8. Find the 10 most repeated words in the romeo_and_juliet.txt
print("=======> Task 8")

print(find_most_common_words("./data/romeo_and_juliet.txt", 10))

# 9. Read the hacker news csv file and find out: a) Count the number of lines containing python or Python b) Count the number lines containing JavaScript, javascript or Javascript c) Count the number lines containing Java and not JavaScript
print("=======> Task 9")

import csv


def count_lines_containing_words(filename, words):
    count = 0
    with open(filename) as file:
        reader = csv.reader(file)
        for row in reader:
            if any(word in row[1] for word in words):
                count += 1
    return count


print(count_lines_containing_words("./data/hacker_news.csv", ["python", "Python"]))
print(
    count_lines_containing_words(
        "./data/hacker_news.csv", ["JavaScript", "javascript", "Javascript"]
    )
)
print(count_lines_containing_words("./data/hacker_news.csv", ["Java", "java"]))
