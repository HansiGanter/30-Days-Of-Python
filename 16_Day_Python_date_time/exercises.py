# 1. Get the current day, month, year, hour, minute and timestamp from datetime module
print("=======> Task 1")

from datetime import datetime

today = datetime.now()
day = today.day
month = today.month
year = today.year
hour = today.hour
minute = today.minute
timestamp = today.timestamp()

print(day, month, year, hour, minute, timestamp)

# 2. Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
print("=======> Task 2")

print(today.strftime("%m/%d/%Y, %H:%M:%S"))

# 3. Today is 5 December, 2019. Change this time string to time.
print("=======> Task 3")

today_string = "5 December, 2019"

print(datetime.strptime(today_string, "%d %B, %Y"))

# 4. Calculate the time difference between now and new year.
print("=======> Task 4")

print(datetime(today.year + 1, 1, 1) - today)

# 5. Calculate the time difference between 1 January 1970 and now.
print("=======> Task 5")

print(today - datetime(1970, 1, 1))

# 6. Think, what can you use the datetime module for? Examples:
print("=======> Task 6")
# - Time series analysis
# - To get a timestamp of any activities in an application
# - Adding posts on a blog
print("Time series analysis")
print("To get a timestamp of any activities in an application")
print("Adding posts on a blog")
