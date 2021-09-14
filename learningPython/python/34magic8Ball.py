import random

name = "Tom"
question = "Will it rain tommorrow?"
answer = " "
random_number = random.randint(1,9)

# print (random_number)

print (name + " asks: " + question)
print ("\n\nThe magic 8-ball rotates to face you, its abyssal coating rippling under the ambient torchlight.\n\n''I have the answers you seek...''\n\nThe 8 ball shakes and trembles the surrounding pillars, ruptures from it's chains, and becomes wholly alighteth in perfect luminescence with the sun that of which you have not seen for days.\n\nCascading through the room, the light dims once more, presenting a small inscription upon the back of your hand. It burns as it writes, but it is worth the answers you had come so far to acquire...\n\nThe inscription reads...\n")

if random_number == 1:
  print("Yes - definitely.")
elif random_number == 2:
  print("It is decidedly so.")
elif random_number == 3:
  print("Without a doubt.")
elif random_number == 4:
  print("Reply hazy, try again.")
elif random_number == 5:
  print("Ask again later.")
elif random_number == 6:
  print("Better not tell you now.")
elif random_number == 7:
  print("My sources say no.")
elif random_number == 8:
  print("Outlook not so good.")
elif random_number == 9:
  print("Very doubtful.")
else:
  print("*beep boop error sound*")