#Write your function here
def exponents(bases, powers):
  newList = []
  for base in bases:
    for power in powers:
      newList.append(base**power)
  return newList

#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))