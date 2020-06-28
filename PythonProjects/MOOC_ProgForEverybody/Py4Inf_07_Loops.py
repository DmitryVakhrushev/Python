
#--================================================
# Loops
#--================================================

#---------------------------------------
# Definite Loop

for i in [5, 4, 3, 2, 1]:
    print(i)
print('Blastoff!')


# A Definite Loop with Strings
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year:',  friend)
print('Done!')


n = 5
while n > 0:
    print(n)
    n -= 1
print('End')
print(n)

#----------------------------------------
# Finishing the iteration with "break"
# The breakstatement ends the current loop and jumps to the
# statement immediately following the loop

while True:
    line = input('> ')
    if line == 'done':
        break

print(line)
print('Done!')

#----------------------------------------
# The iteration with "continue"

# The continue statement ends the current iteration and jumps to the
# top of the loop and starts the next iteration
# continue checks the logic in the "while" again
# so, it's a way to begin execution over in the "while" body without getting all the way to the end first

while True:
    line = input('> ')
    if line[0] == '#':
        print('continue executes and loop starts again')
        continue
    if line == 'done': break
    print("after continue")
print(line)
print('Done!')


