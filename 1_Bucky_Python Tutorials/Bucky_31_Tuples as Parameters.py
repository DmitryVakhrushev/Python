#######################################################
# Bucky_31_Tuples as Parameters
#######################################################

def example(a,b,c):
    return a+b*c

tuna = (5,7,3) # create a tuple

# pass a tuple as a parameter to the function
# we have to use * for tuples and ** for dictionaries

print(example(*tuna))

#-----------------------------
# Example #2

def example2(**this):
    print(this)

bacon = {'mom':32, 'dad':54}

example2(**bacon)
