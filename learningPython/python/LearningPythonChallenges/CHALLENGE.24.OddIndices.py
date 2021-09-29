#Write your function here
def odd_indices(lst):
  newList = []
  for index in range(1, len(lst), 2):
    newList.append(lst[index])
  return newList

#Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))