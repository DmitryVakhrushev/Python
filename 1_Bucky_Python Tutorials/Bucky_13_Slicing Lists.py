#######################################################
# Bucky_13_Slicing Lists
#######################################################

example = list('easyhoss')
print(example)
# ['e', 'a', 's', 'y', 'h', 'o', 's', 's']

# replace characters adfter the 4th character with 'racecars'
example[4:] = list('racecars')
print(example)
# ['e', 'a', 's', 'y', 'r', 'a', 'c', 'e', 'c', 'a', 'r', 's']

#---------------------------------
example = [7,8,9]
print(example)
#[7, 8, 9]

example[1:1]=[3,3,3] # add elements after the first element in the list
print(example)
# [7, 3, 3, 3, 8, 9]

example[1:5]=[] # delete elemets from the 1st till 5th
print(example)
# [7, 9]


