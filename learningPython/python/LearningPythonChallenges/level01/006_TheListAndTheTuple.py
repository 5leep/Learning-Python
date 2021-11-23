# Program which accepts a sequence of comma-separated numbers from user + generate a list and a tuple with the numbers.

# My solution...

values = input("Hello User, please provide me with a set of numbers with commas in-between: ")
list0 = values.split(",")
tuple0 = tuple(list0)
print(tuple0)
print(list0)

# It works!

# Example solution...

values = input("Input some comma seprated numbers : ")
list1 = values.split(",")
tuple1 = tuple(list1)
print('List : ', list1)
print('Tuple : ', tuple1)