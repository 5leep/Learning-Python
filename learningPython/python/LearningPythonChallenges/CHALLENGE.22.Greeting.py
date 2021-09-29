#Write your function here
def add_greetings(names):
  namesList = []
  for name in names:
    namesList.append("Hello, " + name)
  return namesList

#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))