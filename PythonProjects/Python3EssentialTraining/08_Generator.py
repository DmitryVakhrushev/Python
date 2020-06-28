
#-------------------------------------------------------
# Creating sequences with generator functions
#-------------------------------------------------------
def isprime(n):
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True


# Sequence generator. "Yield" is like "Return" but returns a number when isprime(n) is TRUE
# In the WHILE loop the number is checked: if FASLE then n += 1, if TRUE the Prime number is returned
def primes(n = 1):
    # This is an Infinite Loop
    # the loop will be interrupted by a break or return at some point
    while(True):
        if isprime(n): yield n
        n += 1


for n in primes():
    if n > 100: break
    print(n)