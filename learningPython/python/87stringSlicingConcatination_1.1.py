first_name = "Reiko"
last_name = "Matsuki"

def password_generator(first_name, last_name):
  temp_password = first_name[-3:] + last_name[-3:]
  return str(temp_password)

temp_password = password_generator(first_name, last_name)

print(temp_password)