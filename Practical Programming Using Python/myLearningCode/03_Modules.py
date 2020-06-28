#===============================================================================
# Modules (p.41)
#===============================================================================

# A MODULE is a collection of functions that are groupped together in a single file.
# As several modules may contain a function with the same name
# we have to explicitly name the module and the function, e.g. math.sqrt(50)

'''
import math

print(math.sqrt(50))
print(math.pi)

radius = 5
print('area is %6f' % (math.pi * radius**2))
# print(help(math)) # buily-in help
'''
#------------------------------------------------------------------------------ 

# You can import just a part of the module (not) the whole module

# e.g. we can import sqrt() function
# to use it we must not specify a module name
from math import sqrt

print (sqrt(49))
# print (pi)

# ---> Standard Python Libraries: http://docs.python.org/3/library/index.html

# We can also import any file we have (do not include .py extension)
import myModule01

print(myModule01.to_celsius(100))


import myModule01

print("myM: __name__ is", __name__)


