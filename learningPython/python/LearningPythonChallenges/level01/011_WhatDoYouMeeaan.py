# Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).

wha = input("What syntax would you like to find: ")
print("\n" + str(help(input)))

# It works!


# Example solution...

print(abs.__doc__)


# My amended solution...

wha = input("What syntax would you like to find: ")
print("\n" + str(input.__doc__))