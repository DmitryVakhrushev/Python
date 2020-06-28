
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


# -------------------------------------------------
# Reusing code with a function
# Lesson 07 -- Create a function
# -------------------------------------------------
def isprime(n):
    if n == 1:
        print("1 is special")
        return False
    for x in range(2,n):
        if n % x == 0:
            print("{} equals {} x {}".format(n, x, n//x))
            return False
    else:
        print(n, "is a prime number")
        return True

# -------------------------------------------------
# Use the function
for n in range(1, 20):
    isprime(n)

    

    
#-------------------------------------------------------------------------------------------------
# Lesson 06 -- While Loop
#-------------------------------------------------------------------------------------------------

# sum of two elements defines the next set
# Fibinacchi series

a, b = 0, 1
while b < 50:
    print(b)
    a, b = b, a+b

# For Loop

# Read the kines from the file
# "Iterator" is the object which gives you the new value each time it's called

fh = open('lines.txt')
for line in fh.readlines():
    print(line, end='')
	

#-------------------------------------------------------
# Lesson 08. Creating sequences with generator functions
#-------------------------------------------------------
def isprime(n):
    if n == 1:
        return False
    for x in range(2,n):
        if n % x == 0:
            return False
    else:
        return True


# Sequence generator. "Yield" is like "Return"
def primes(n = 1):
    while(True):
        if isprime(n): yield n
        n += 1


for n in primes():
    if n > 100: break
    print(n)