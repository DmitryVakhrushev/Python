#--------------------------------
# Coursera_26_list Methods 
#--------------------------------

# get the methods in the "list"
# print(dir(list))

# "append" method -- to add smth to the list
'''
#   >>> blue
#    >>> yellow
#    >>> brown
'''

colors = []
prompt = 'Enter another  one of your favorite colours (type return to end): '
col = input(prompt)
while col !='':
    colors.append(col)
    col = input(prompt)

print(colors)

input("press any key")

# "extend" method -- to alter the lest
# "extend" works with the list
# colors.extend('black','white') --> will generate an error
# colors.extend(['black','white']) --> correct!

colors.extend(['hot pink','neon green'])
print(colors)

input("press any key")

# "pop" method deletes the last element AND returns it (we can use to assign it)
colors.pop()
print(colors)

colors.pop(2) # removing "brown" from the list
print(colors)

#------------------------------
# Examine if a color exists in the list. Then we can remove it
if colors.count('yellow')>0:
    colors.remove('yellow')
print(colors)

# another more standard variant
if 'yellow' in colors:
    colors.remove('yellow')
#---------------------------------
colors.extend(['auburn','taupe','magenta'])
print(colors)

colors.reverse()
print(colors)
#-------------------------------------
# "Insert" method
insert.colors(-2,'brown') # we do not replace the item at index 2
# instead the list is shifted giving a space for 'brown'
print(colors)

#--------------------------
# Index method -- returns the index of the object
if 'hot pink' in colors:
    where = colors.index('hot pink')
    colors.pop(where)
print(colors)









