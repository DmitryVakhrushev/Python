
#===============================================================================
# 3-3: Guess and Check for Lists -- Kent D. Lee
#===============================================================================

# Check if a number between 2 and 49 is a PRIME number

primes = [2,3,5,7]

print(primes)

x = int(input('Please enter an integer between 2 and 49: '))

# Make a guess
isPrime = True

# Go through the list to check if our guess is wrong

for p in primes:
    # check if there is no remainder then
    # the number x s the prime
    if x % p == 0 and not x in primes:
        isPrime = False
        
if isPrime:
    print(x, "is prime.")
else:
    print(x, "is NOT prime.")
        
        
