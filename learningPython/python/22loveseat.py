lovely_loveseat_description = """\nLovely Loveseat. \nTufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.
"""
lovely_loveseat_price = 254.00

stylish_settee_description = """\nStylish Settee. \nFaux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.
"""
stylish_settee_price = 180.50

luxurious_lamp_description = """\nLuxurious Lamp. \nGlass and iron. 36 inches tall. Brown with cream shade.
"""
luxurious_lamp_price = 52.15


sales_tax = 0.088


customer_one_total = 0
customer_one_itemization = ""
customer_one_total = lovely_loveseat_price
customer_one_itemization = lovely_loveseat_description
customer_one_total = lovely_loveseat_price + luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description
customer_one_tax = customer_one_total * sales_tax
customer_one_total + lovely_loveseat_price + luxurious_lamp_price + customer_one_tax

print ("\n\n\nCustomer One Items:")
print (customer_one_itemization)
print ("\nCustomer One Total:\n")
print (customer_one_total)

print ("\n\n\n")