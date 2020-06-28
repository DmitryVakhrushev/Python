
# Bill Weinman "Python 3 Essential Training"

#-------------------------------------------------------------------------------------------------
# Lesson 05 -- Selecting code with conditionals
#-------------------------------------------------------------------------------------------------

a, b = 3, 1 # assign multiple values at a time to several variables

if a < b:
    print('a ({}) is less than b({})'.format(a,b)) # "format" is a method for the string object
else:
    print('a ({}) is not less than b({})'.format(a,b))

#-------------------------------------------------------------------------------------------------
# Print using the "format" method for the string objects
arg1 = "Dmitry"
arg2 = "day"
z = "Hi {}! How is your {}?"
print(z.format(arg1,arg2))

#-------------------------------------------------------------------------------------------------
# Conditional Expressions (similar to C-base languages)
print("foo" if a < b else "bar")


