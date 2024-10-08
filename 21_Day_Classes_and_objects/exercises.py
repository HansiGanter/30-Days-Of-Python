#####################
# Exercise: Level 1
#####################

# 1. Python has the module called statistics and we can use this module to do all the statistical calculations. However, to learn how to make function and reuse function let us try to develop a program, which calculates the measure of central tendency of a sample (mean, median, mode) and measure of variability (range, variance, standard deviation). In addition to those measures, find the min, max, count, percentile, and frequency distribution of the sample. You can create a class called Statistics and create all the functions that do statistical calculations as methods for the Statistics class. Check the output below.
print("=======> Task 1")

ages = [
    31,
    26,
    34,
    37,
    27,
    26,
    32,
    32,
    26,
    27,
    27,
    24,
    32,
    33,
    27,
    25,
    26,
    38,
    37,
    31,
    34,
    24,
    33,
    29,
    26,
]


class Statistics:
    def __init__(self, data):
        self.data = data

    def count(self):
        return len(self.data)

    def sum(self):
        return sum(self.data)

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def range(self):
        return max(self.data) - min(self.data)

    def mean(self):
        return sum(self.data) / len(self.data)

    def median(self):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        if n % 2 == 1:
            return sorted_data[n // 2]
        else:
            return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2

    def mode(self):
        frequency = {}
        for value in self.data:
            if value in frequency:
                frequency[value] += 1
            else:
                frequency[value] = 1
        if not frequency:
            return None, 0
        mode = max(frequency.keys(), key=lambda k: frequency[k])
        return mode, frequency[mode]

    def std(self):
        mean = self.mean()
        variance = sum((x - mean) ** 2 for x in self.data) / len(self.data)
        return variance**0.5

    def var(self):
        mean = self.mean()
        return sum((x - mean) ** 2 for x in self.data) / len(self.data)

    def freq_dist(self):
        frequency = {}
        for value in self.data:
            if value in frequency:
                frequency[value] += 1
            else:
                frequency[value] = 1
        return sorted(frequency.items(), key=lambda x: x[1], reverse=True)

    def describe(self):
        return {
            "Count": self.count(),
            "Sum": self.sum(),
            "Min": self.min(),
            "Max": self.max(),
            "Range": self.range(),
            "Mean": self.mean(),
            "Median": self.median(),
            "Mode": self.mode(),
            "Standard Deviation": self.std(),
            "Variance": self.var(),
            "Frequency Distribution": self.freq_dist(),
        }


data = Statistics(ages)

print("Count:", data.count())  # 25
print("Sum: ", data.sum())  # 744
print("Min: ", data.min())  # 24
print("Max: ", data.max())  # 38
print("Range: ", data.range())  # 14
print("Mean: ", data.mean())  # 30
print("Median: ", data.median())  # 29
print("Mode: ", data.mode())  # {'mode': 26, 'count': 5}
print("Standard Deviation: ", data.std())  # 4.2
print("Variance: ", data.var())  # 17.5
print(
    "Frequency Distribution: ", data.freq_dist()
)  # [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]

# your output should look like this
print(data.describe())
# Count: 25
# Sum:  744
# Min:  24
# Max:  38
# Range:  14
# Mean:  30
# Median:  29
# Mode:  (26, 5)
# Variance:  17.5
# Standard Deviation:  4.2
# Frequency Distribution: [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]

#####################
# Exercise: Level 2
#####################

# 2. Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties and it has total_income, total_expense, account_info, add_income, add_expense and account_balance methods. Incomes is a set of incomes and its description. The same goes for expenses.
print("=======> Task 2")


class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = {}
        self.expenses = {}

    def total_income(self):
        return sum(self.incomes.values())

    def total_expense(self):
        return sum(self.expenses.values())

    def account_info(self):
        return f"Account belongs to {self.firstname} {self.lastname}."

    def add_income(self, description, amount):
        self.incomes[description] = self.incomes.get(description, 0) + amount

    def add_expense(self, description, amount):
        self.expenses[description] = self.expenses.get(description, 0) + amount

    def account_balance(self):
        return self.total_income() - self.total_expense()


person = PersonAccount("John", "Doe")
person.add_income("Salary", 1000)
person.add_income("Freelance", 500)
person.add_expense("Rent", 100)
person.add_expense("Food", 50)

print(person.account_info())  # Account belongs to John Doe.
print(person.total_income())  # 1500
print(person.total_expense())  # 150
print(person.account_balance())  # 1350
