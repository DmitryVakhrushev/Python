#######################################################
# Bucky 12_More List Functions 
#######################################################

numbers = [8,1,4,17,28,165,7]
print(numbers)

print(len(numbers)) # getting the length of the list
print(min(numbers))
print(max(numbers))

print(list('bucky')) # converts any string to a list
print(list('21'))

# changing a specific value in the list
numbers[3] = 77 # changing 17 to 77
print(numbers)

# delete an element from the list
del numbers[3]
print(numbers)


