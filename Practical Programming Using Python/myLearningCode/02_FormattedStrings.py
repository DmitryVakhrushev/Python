#===============================================================================
# Python data types
#===============================================================================

# ********   str, float, int, bolean *************

# Escape character "\"
# \n -- end of line, \t -- tabulation
print ('one \t two \n three \n')

#===============================================================================
# Formatted printing (p.36)
#===============================================================================

rabbits = 17
cage = 10
print("%f rabbits are in cage #%d. " % (rabbits,cage))

print ("[%i, %i, %i]" % (1, 2, 3))

print("The {} who say {}".format('Knights','Hi'))
print("The {0} who say {1}".format('Knights','Hi'))
print("The {1} who say {0} \n".format('Knights','Hi'))

print("I ate {} {}!!!".format(50,'apples'))
print("I ate {0} {1}!!!".format(50,'apples')) # {0} takes 50 and {1} takes 'apples'
print("I ate {0:5} {1:20}!!!".format(50,'apples')) # add extra spaces after the argument
print("I ate {0:5.2f} {1}!!! \n".format(50.259,'apples')) # round to 2 decimal points

# print("".format()) -- general format

for i in range(11):
    print("{0} {1} {2}".format(i,i*i,i*i*i))

print()

for i in range(11):
    print("{0:2d} {1:3d} {2:4d}".format(i,i*i,i*i*i))
    
print()
#===============================================================================
# String Methods
#===============================================================================
a = 'This is My favorite Game!'
print(a.upper())
print(a.swapcase())

def myF(x):
    x +=10
    return x

print(myF(25))
    


