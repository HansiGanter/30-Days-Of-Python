import requests
from bs4 import BeautifulSoup

# 1. Scrape the following website and store the data as json file(url = 'http://www.bu.edu/president/boston-university-facts-stats/').

print("=======> Task 1")

url = "http://www.bu.edu/president/boston-university-facts-stats/"

response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, "html.parser")
print(soup.prettify())

# 2. Extract the table in this url (https://archive.ics.uci.edu/ml/datasets.php) and change it to a json file
print("=======> Task 2")

url = "https://archive.ics.uci.edu/ml/datasets.php"

response = requests.get(url)
print("Status Code: ", response.status_code)
if response.status_code == 200:
    content = response.content
    soup = BeautifulSoup(content, "html.parser")
    tables = soup.find_all("table", {"class": "wikitable sortable"})

    if tables:
        table = tables[0]  # the result is a list, we are taking out data from it
        for td in table.find("tr").find_all("td"):
            print(td.text)


# 3. Scrape the presidents table and store the data as json(https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States). The table is not very structured and the scrapping may take very long time.
print("=======> Task 3")

url = "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"

response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, "html.parser")

tables = soup.find_all("table")

if tables:
    table = tables[0]
    thead = list(
        filter(
            lambda y: y != "\n",
            list(map(lambda x: x.get_text(), [tr for tr in table.find("tr")])),
        )
    )
    tbody = [tr for tr in table.find_all("tr")]

    json = []

    for tr in tbody:
        new_item = {}
        for idx, td in enumerate(tr.find_all("td")):
            new_item[thead[idx]] = td.get_text()

        json.append(new_item)

    print(json)
