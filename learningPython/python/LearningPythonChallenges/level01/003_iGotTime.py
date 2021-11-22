# My solution...

import datetime

import day as day

time0 = datetime.datetime.now()
print("\nThe current date and time is:\n" + time0.strftime("%c"))

# It works!


# Example solution...

import datetime

time1 = datetime.datetime.now()
print("\nCurrent date and time : ")
print(time1.strftime("%Y-%m-%d %H:%M:%S"))

# My amended solution 1.0

import datetime

time2 = datetime.datetime.now()
print("\nHello Mx\nIt is " + time2.strftime("%H:%M on the %d of %B %G \nHave a nice day ;)"))

# My amended solution 2.0

import datetime

now = datetime.datetime.now()


def suffix(day):
    suffix = ""
    if 4 <= day <= 20 or 24 <= day <= 30:
        suffix = "th"
    else:
        suffix = ["st", "nd", "rd"][day % 10 - 1]
    return suffix


print("\nHello Mx\nIt is " + time2.strftime("%H:%M on the %d" + suffix(now.day) + " of %B %G \nHave a nice day ;)"))

# It works!