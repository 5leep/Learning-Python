weight = 8.4
cost = 0
groundFlatCharge = 20.00
groundPremium = 125.00

# GROUND SHIPPING
if weight < 0:
  print("A package cannot be negative in weight. Please enter a valid weight")
elif weight <= 2:
  cost = weight*1.50
elif weight <= 6:
  cost = weight*3.00
elif weight <= 10:
  cost = weight*4.00
elif weight > 10:
  cost = weight*4.75
else:
  print("Error")

print ("Ground Shipping =",cost + groundFlatCharge + groundPremium)


# DRONE SHIPPING
if weight < 0:
  print("A package cannot be negative in weight. Please enter a valid weight")
elif weight <= 2:
  cost = weight*4.50
elif weight <= 6:
  cost = weight*9.00
elif weight <= 10:
  cost = weight*12.00
elif weight > 10:
  cost = weight*14.25
else:
  print("Error")

print ("Drone Shipping =",cost)
