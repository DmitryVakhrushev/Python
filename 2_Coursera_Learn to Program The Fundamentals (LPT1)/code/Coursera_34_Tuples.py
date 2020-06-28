#-----------------------------------------
# Coursera_34_Tuples
#-----------------------------------------
# Tuples are Immutable Sequences -- we cannot change them
# we can count or index them

print(dir(tuple))
tup = ('a', 3, -0.2)
print(tup)

# We can index tuples
print(tup[0])
print(tup[1])

# We can slice tuples
print(tup[:2])
print(tup[1:3])

# We can iterate through the tuple's items
for x in tup:
    print(x)

print(len(tup))
for x in range(len(tup)):
      print(tup[1])

# two-element tuple
z = (1,2)
print(z)

# one-element tuple. Put a comma after a number
y = (1,)
print(y)
