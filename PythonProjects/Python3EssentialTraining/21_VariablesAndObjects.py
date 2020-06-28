
#-----------------------------------------------------
# 21. Understanding variables and objects in Python
#-----------------------------------------------------

x = 43
print(id(x))
print(type(x))


#-----------------------------------------------------
# 22. mutable and immutable objects
#-----------------------------------------------------

# Variables in Python are referances to different objects

print("---------------------------------------")

z = 77
print(id(z))
z = 79
print(id(z))