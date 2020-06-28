#######################################################
# Bucky_15 - More Methods
#######################################################

#-----------------------------------------------
# Index methods in the list or sequence

say = ['Hey', 'now', 'brown', 'cow']
print(say)
# ['Hey', 'now', 'brown', 'cow']

#-----------------------------------------------
# Shows the index of the object in the list
print(say.index('brown'))
# 2

#-----------------------------------------------
# Inserts an object
say.insert(2,'hoss')
print(say)
# ['Hey', 'now', 'hoss', 'brown', 'cow']

#-----------------------------------------------
# Removes an object and shows it
print(say.pop(1)) # it removes and returns the removed object
print(say)
# now
# ['Hey', 'hoss', 'brown', 'cow']

#-----------------------------------------------
# Removes an object
say.remove('brown') # if print returns 'None'
print(say)
# ['Hey', 'hoss', 'cow']

#-----------------------------------------------
# Reverse a string
say.reverse()
print(say)
# ['cow', 'hoss', 'Hey']
