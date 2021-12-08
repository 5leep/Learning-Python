# Python program to calculate number of days between two dates.

# My solution...

from datetime import date

dateFrom = date(2021, 12, 8)
dateTo = date(2021, 12, 17)
daysBetween = dateTo - dateFrom
print("There are " + str(daysBetween.days) + " days between " + str(dateFrom.strftime("%B ")) + str(dateFrom.day) + " and " + str(dateTo.strftime("%B ")) + str(dateTo.day) + ".")

# It works!


# Example solution...

from datetime import date
f_date = date(2014, 7, 2)
l_date = date(2014, 7, 11)
delta = l_date - f_date
print(delta.days)
