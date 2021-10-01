from random import randint

# Define your functions
def coffee_bot():
  names=["James", "Michael", "Brian", "Andrew", "Name"]
  print("""
         o      
    \   /
 ,-.'---`.__ 
((j`=====',-'
 `-\     /
    `-=-'     CoffeeBot.py
  """)
  print("\nWelcome to the  cafe! :)")
  size = get_size()
  drink_type = get_drink_type()
  print("\n\nAlright, there's a {} {} coming right up! ;)\n".format(size, drink_type))
  name = input("Can I get your name please?\n\n   You're name > ")
  print("\nThank you " + name + "! You're product is just coming.\n")
  print("""
               ;,'
     _o_    ;:;'
 ,-.'---`.__ ;
((j`=====',-'
 `-\     /
    `-=-'     CoffeeBot.py
  """)

def get_size():
  res = input("\nWhat size coffee would you like?\n\n[a] Small \n[b] Medium \n[c] Large \n\n> ")
  if res == "a":
    return "Small"
  if res == "b":
    return "Medium"
  if res == "c":
    return "Large"
  else:
    print_message()
    return get_size()

def print_message():
  print ("\nI'm sorry, I did not understand your selection. Please enter the corresponding letter for your response")

def get_drink_type():
  res = input("What type of drink would you like?\n\n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n\n")
  if res == "a":
    return "Brewed Coffee\n"
  elif res == "b":
    return "Mocha\n"
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