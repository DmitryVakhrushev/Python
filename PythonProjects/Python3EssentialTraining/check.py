



n = 6

for x in range(2,n):
    print(x)

for x in range(2,n):
    if n % x == 0:
        print("Not prime")
    else:
        print("Is PRIME!!!")

print('-----------------------------------------')

# the loop will be interrupted by a break or return at some point.
def myFunc(z):
    while(True):
        z *= 3
        if z > 20: return z

z = 5
print(myFunc(z))

z = 1
print(myFunc(z))
