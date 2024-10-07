# 1. Read this url and find the 10 most frequent words. romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
print("=======> Task 1")
import requests

romeo_and_juliet = "http://www.gutenberg.org/files/1112/1112.txt"

response = requests.get(romeo_and_juliet)


def ten_most_frequent_words(response):
    words = response.text.split()
    words = [word.lower() for word in words]
    words = filter(lambda word: word.isalpha(), words)
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:10]


print(ten_most_frequent_words(response))

# 2. Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :
print("=======> Task 2")
#  i. the min, max, mean, median, standard deviation of cats' weight in metric units.

cats_api = "https://api.thecatapi.com/v1/breeds"

response = requests.get(cats_api).json()

import statistics


def min_max_mean_median_std_weight(response):
    weights = [
        (
            int(cat["weight"]["metric"].split("-")[0])
            + int(cat["weight"]["metric"].split("-")[1])
        )
        / 2
        for cat in response
    ]
    return (
        min(weights),
        max(weights),
        sum(weights) / len(weights),
        statistics.median(weights),
        statistics.stdev(weights),
    )


print(min_max_mean_median_std_weight(response))


#  ii. the min, max, mean, median, standard deviation of cats' lifespan in years.
def min_max_mean_median_std_lifespan(response):
    lifespans = [
        (int(cat["life_span"].split("-")[0]) + int(cat["life_span"].split("-")[1])) / 2
        for cat in response
    ]
    return (
        min(lifespans),
        max(lifespans),
        sum(lifespans) / len(lifespans),
        statistics.median(lifespans),
        statistics.stdev(lifespans),
    )


print(min_max_mean_median_std_lifespan(response))


# iii. Create a frequency table of country and breed of cats
def frequency_table_country_breed(response):
    frequency_table = {}
    for cat in response:
        if cat["origin"] in frequency_table:
            frequency_table[cat["origin"]] += 1
        else:
            frequency_table[cat["origin"]] = 1
    return frequency_table


print(frequency_table_country_breed(response))

# 3. Read the countries API and find
print("=======> Task 3")

#  i. the 10 largest countries
response = requests.get("https://restcountries.com/v3.1/all").json()


def ten_largest_countries(response):
    areas = [(country["area"], country["name"]["common"]) for country in response]
    return sorted(areas, reverse=True)[:10]


print(ten_largest_countries(response))


#  ii. the 10 most spoken languages
def ten_most_spoken_languages(response):
    languages = {}
    for country in response:
        if "languages" in country:
            for lang in country["languages"].values():
                languages[lang] = languages.get(lang, 0) + 1
    return sorted(languages.items(), key=lambda x: x[1], reverse=True)[:10]


print(ten_most_spoken_languages(response))


#  iii. the total number of languages in the countries API
def total_number_of_languages(response):
    languages = {}
    for country in response:
        if "languages" in country:
            for lang in country["languages"].values():
                languages[lang] = languages.get(lang, 0) + 1
    return len(languages)


print(total_number_of_languages(response))

# 4. UCI is one of the most common places to get data sets for data science and machine learning. Read the content of UCL (https://archive.ics.uci.edu/ml/datasets.php). Without additional libraries it will be difficult, so you may try it with BeautifulSoup4
print("=======> Task 4")

from bs4 import BeautifulSoup


def get_uci_datasets(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup.find_all("a", href=True)


print(get_uci_datasets("https://archive.ics.uci.edu/ml/datasets.php"))
