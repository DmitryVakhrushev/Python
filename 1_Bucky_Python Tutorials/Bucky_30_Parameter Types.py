#######################################################
# Bucky_30_Parameter Types
#######################################################

# Converting to a dictionary with **

def cart(**items):
    print(items)

cart(apples=4, peaches=6, beef=60)
cart(apples=4, peaches=6, beef=60)

#--------------------------------------

def profile(first, last, *ages, **items):
    print(first, last)
    print(ages)
    print(items)

profile('bucky','roberts',32,43,65,76, bacon=4, beef=6, sausage=64)
