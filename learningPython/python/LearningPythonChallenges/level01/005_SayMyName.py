# Python program that accepts the user's first and last name and print them in reverse order with a space between them.

# My method..

userForename = str(input("Hello User :)\nwhat is your forename?\n\nNAME: "))
userForename = str.capitalize(userForename)
print("Good to see you " + userForename + "!")
userSurname = str(input("And what is your last name?\n\nSURNAME: "))
print("My specifications state that I log you as\n\n'" + str.upper(userSurname) + "', '" + userForename + "'")
print("\nIt was nice to meet you, " + userForename + "!" + "\nYou can call me EV ;)")

# It works!

# Example solution...

fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print ("Hello " + lname + " " + fname)