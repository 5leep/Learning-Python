# Write a Python program to accept a filename from the user and print the extension of that.

# My solution...

file = input("What file are you referring to? (e.g. abc.java) : ")
extension = file.split(".",1)[-1]
print("The extension to " + file + " is " + extension)

# It works! (somewhat)

# Their solution...

filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))
