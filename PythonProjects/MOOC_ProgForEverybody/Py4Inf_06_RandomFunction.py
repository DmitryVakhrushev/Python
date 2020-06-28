

# This program produces the following list of 10 random numbers between 0.0
# and up to but not including 1.0.

import random
import math

for i in range(10):
    x = random.random()
    print(x)

print("--------------------------------------")

# randint takes parameters low and high
# and returns an integer between low and high (including both).
print(random.randint(5, 10))

print("--------------------------------------")
# To choose an element from a sequence at random, you can use choice:
t = [1, 2, 3]
print(random.choice(t))


print(math.pi)


# --- VOID functions
# Void functions might display something on the screen or have some other effect,
# but they don’t have a return value.