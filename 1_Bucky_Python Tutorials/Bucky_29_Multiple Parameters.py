#######################################################
# Bucky_29_Multiple Parameters
#######################################################

#---------------------------
# Allows just one parameter
def note1(x):
    print(x)

note1('beef')

# note1('beef','oil') # --> will produce an error

#---------------------------
# Allows multiple parameters

def mynote(*food):
    print(food)

mynote('apples')
mynote('apples','peaches','beef')

#------------------------------------
def profile(name, *ages):
    print(name)
    print(ages)

profile('bucky', 42,43,76,54,98)
