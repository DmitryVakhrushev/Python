#######################################################
# Bucky_26_ Infinite Loops and Break
#######################################################

ages = {'dad':42, 'mom':48, 'lisa':7}
print(ages)

# Printing keys
for i in ages:
    print(i)

# Printing values for ech key
for i in ages:
    print(i, ages[i])

#--------------------------------
# breaking a loop
#--------------------------------

# Infinite loop

while 1:
    name = input('Enter your name: ')
    if name == 'quit': break
    
    
