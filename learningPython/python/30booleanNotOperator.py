statement_one = False

statement_two = True

name = "Tom"

credits = 120
gpa = 1.8

print ('\n\n\n' + 'Hello ' + name + ', the following message regards your college "Grade Point Average" (GPA) and Credit awarded by your efforts.' + '\n')

if not credits >= 120:
  print("You do not have enough credits to graduate.\n\n")

if not gpa >= 2.0:
  print("Your GPA is not high enough to graduate.\n\n")

if not (credits >= 120) and not (gpa >= 2.0):
  print("You do not meet either requirement to graduate!\n\n")