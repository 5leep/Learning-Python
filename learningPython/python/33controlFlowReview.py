print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")
 
fighter = "Tornado Tom"
weight = 185.00
planet = 3
opponent = ""

# Write an if statement below:

if planet == 1:
  planet = str("Venus")
  weight = weight * 0.91
  opponent = "Vorg the Venus Vidicator"
elif planet == 2:
  planet = str("Mars")
  weight = weight * 0.38
  opponent = "Marcus the Marauder"
elif planet == 3:
  planet = str("Jupiter")
  weight = weight * 2.34
  opponent = "Justicer Julaer"
elif planet == 4:
  planet = str("Saturn")
  weight = weight * 1.06
  opponent = "Spectre Sarliv"
elif planet == 5:
  planet = str("Uranus")
  weight = weight * 0.92
  opponent = "Urik the Undertaker"
elif planet == 6:
  planet = str("Neptune")
  weight = weight * 1.19
  opponent = "Nightstar Nurdle"
else:
  print ("Sorry ",fighter," I don't have any information about that.\n but your Earth weight is currently ", weight)

print ("Hello, " + fighter + "!","\nyour weight on " + planet + " is:",weight,"lbs\n\nYou will be fighting:\n\n" + opponent + "\n\ngood luck out there! :)\n\n")