
#------------------------------------------------------
# Dictionaries
#------------------------------------------------------
# Dictionaries are Python`s most powerful data collection
# Dictionaries allow us to do fast database-like operations in Python

# Dictionaries have different names in different languages
    # Associative Arrays - Perl / Php
    # Properties or Map or HashMap - Java
    # Property Bag - C# / .Net

purse= dict()
purse['money']= 12
purse['candy']= 3
purse['tissues']= 75
print(purse)

# In Dictionaries we use labels (KEYs)
print(purse['candy'])

purse['candy']= purse['candy'] + 2
print(purse['candy'])

# Compare LISTS and DICTIONARIES

# LIsts maintain order
lst = list()
lst.append(21)
lst.append(183)
print(lst) #[21, 183]
lst[0] = 23
print(lst) # [23, 183]

# Dictionaries doesn't have order
ddd =dict()
ddd['age'] = 21
ddd['course'] = 182
print(ddd) # {'course': 182, 'age': 21}
ddd['age'] = 23
print(ddd) # {'course': 182, 'age': 23}

########################################
# Counting

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    if name not in counts: # the dictionary doesn't have this KEY
        counts[name] = 1 # create a KEY and assign 1 to it
    else:
        counts[name] = counts[name] + 1 # if the key exists add 1 to its count

print(counts)


############################################
# The "get" method for dictionaries

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)






