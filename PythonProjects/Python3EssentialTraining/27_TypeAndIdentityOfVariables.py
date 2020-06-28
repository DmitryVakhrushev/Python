
#------------------------------------------------------------
# Lesson #27: Finding the type and identity of a variable
#------------------------------------------------------------

# Everything in Python 3 is an object


#-------------------------------------------------------------------
# Immutable objects, e.g. numbers
x = 42
print(id(x)) # 507100096
print(type(x))

# the number of 42 is an object:
# It has (1) ID, (2) Type, and (3) Value

# if we assign 42 to y it will be exactly the same object
y = 42
id(y)  # 507100096

print(x == y) # compares values
print(x is y) # compares IDs

#-------------------------------------------------------------------
# Unique ID refers to a specific object
# For Mutable objects the IDs are different

x = dict(x=42)
y = dict(x=42)

print(x == y) # True
print(x is y) # False

#-------------------------------------------------------------------
a,b = 0,1
print(a == b) # False
print(a < b) # True
print(a > b) # False

a = True
print(type(a)) # <class 'bool'>
print(id(a))    # 506662104
print(id(True)) # 506662104 -- the same id

