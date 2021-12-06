# Write a Python program to print the calendar of a given month and year.

# My solution...

import calendar


def showMeThatCalendar(year, month):
    return calendar.month(year, month)


print("\nHello Mx, please provide me with a year and a month in number format. E.g. year = 2021, month = 12 :)\n")
year = (int(input("Give me a year: ")))
month = (int(input("Give me a month: ")))

print("\n", showMeThatCalendar(year, month))

# It works!


# Example solution...

import calendar
y = int(input("Input the year : "))
m = int(input("Input the month : "))
print(calendar.month(y, m))