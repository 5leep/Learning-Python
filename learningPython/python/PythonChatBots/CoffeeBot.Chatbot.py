

def coffee_bot():
  names=["James", "Michael", "Brian", "Andrew", "Name"]
  print("\nWelcome to the  cafe! :)")
  cost = 0.00
  cost = get_size(cost)
  size = get_size()
  drink_type = get_drink_type()
  cup = get_cup()
  print("\nAlright, there's a {} {} coming right up, in a {} cup!".format(size, drink_type, cup))
  name = input("\nCan I get your name please?\n\n> ")
  print("\nThank you " + name + "! Your {} {} is just coming, which will be a total of £{}".format(size, drink_type, cost))
  print("\nFeel free to take a seat while we get that for you\n;)\n")
  print("""
               ;,'
     _o_    ;:;'
 ,-.'---`.__ ;
((j`=====',-'
 `-\     /
    `-=-'     CoffeeBot.py
  """)

def get_size(cost):
  cost = float
  res = input("\nWhat size coffee would you like?\n\n[a] Small \n[b] Medium \n[c] Large \n\n> ")
  if res == "a":
    return "Small" and cost == 1.50
  if res == "b":
    return "Medium" and cost == 2.00
  if res == "c":
    return "Large" and cost == 2.25
  else:
    print_message()
    return get_size()

def get_cup():
  res = input("\nWhat cup type would you prefer??\n\n[a] Plastic \n[b] Reusable \n[c] Plastic bag \n\n> ")
  if res == "a":
    return "Plastic"
  if res == "b":
    return "Reusable"
  if res == "c":
    return "Wooden"
  else:
    print_message()
    return get_cup()

def print_message():
  print ("\nI'm sorry, I did not understand your selection. Please enter the corresponding letter for your response")

def get_drink_type():
  res = input("What type of drink would you like?\n\n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n\n")
  if res == "a":
    return "Brewed Coffee"
  elif res == "b":
    return "Mocha"
  elif res == "c":
    return order_latte()
  else:
    print_message()
    return get_drink_type()

def order_latte():
  res = input("And what kind of milk for your latte?\n\n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk\n\n")
  if res == "a":
    return "Latte"
  elif res == "b":
    return "Non-fat Latte"
  elif res == "c":
    return "Soy Latte"
  else:
    print_message()
    return order_latte()

# Call coffee_bot()!
coffee_bot()
