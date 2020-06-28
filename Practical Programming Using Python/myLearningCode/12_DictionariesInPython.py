#===============================================================================
# 4-3: Dictionaries in Python -- Kent D.Lee
#===============================================================================

#----------------------------------------- 
# This is a list
#-----------------------------------------
myList = [] # empty list
lst = ['Kent','Sophus','Lee']

print(lst[0])
for name in lst:
    print(name)

print("-------------------------------------------")  

#-----------------------------------------
# This is a dictionary
#-----------------------------------------
# A dictionary has a "Key" and value(s) associated with the key  
# Keys have to be UNIQUE

dictionary = {} # An empty dictionary

dictionary['Kent'] = 0
dictionary['Sophus'] = 1
dictionary['Lee'] = [4,6,7]

print(dictionary)


# there is no order in a dictionary when printing keys
for key in dictionary:
    print(key)

# printing keys and values
for key in dictionary:
    print(key, dictionary[key])

print("-------------------------------------------")  
pets = {}
pets['Kent'] = 'Mesa'
pets['Sophus'] = 'Smudge'
pets['Lee'] = 'Lassie'

for owner in pets:
    print(owner, pets[owner])
