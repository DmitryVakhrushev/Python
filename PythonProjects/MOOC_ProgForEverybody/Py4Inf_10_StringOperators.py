
#==============================================================================
# String Operators
#==============================================================================


fruit = 'banana'
print(type(fruit))
print('first char:',fruit[0])
print('middle chars:',fruit[2:4])
print('last char:',fruit[-1])

print('length:', len(fruit), sep=' ')
# help(print)

length = len(fruit)
print(length)


dir(str) # to check all methods of that object
dir(fruit) # e.g.

#------------------------------------------------------------------------------
# Traversal (пересечение) -- processing a string one character at a time
#------------------------------------------------------------------------------
# One approach -- WHILE Loop
fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1


fruit = 'pineapple'
index = len(fruit)-1
while index >= 0:
    print(fruit[index])
    index -= 1

print("--------------------------")

# Second option
for char in fruit:
    print(char)

print("--------------------------")
# Looping and counting
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)

print("--------------------------")
# The in operator

print('a' in 'banana')
print('seed' in 'banana')



print("------- String Methods -------")

# str.capitalize()
# str.center(width[, fillchar])
# str.endswith(suffix[, start[, end]])
# str.find(sub[, start[, end]])
# str.lstrip([chars])
#
# str.replace(old, new[, count])
# str.lower()
# str.rstrip([chars])
# str.strip([chars])
# str.upper()

word = 'banana'
index = word.find('a')
print(index)

line = '     Here we go '
print(line)
line = line.strip() # remove white space (spaces, tabs, or newlines) from the beginning and end of a string
print(line) #'Here we go'


print("------- Parsing strings -------")
# Often, we want to look into a string and find a substring.
data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print (atpos) # 21
sppos = data.find(' ',atpos)
print(sppos) # 31
host = data[atpos+1:sppos]
print(host) # uct.ac.za


print("------- Format operator -------")
# Format operator, {} allows us to construct strings, replacing parts of the
# strings with the data stored in variables.

animalCount = 17
s = 'I spotted {} camels'.format(animalCount)
print(s)

################################################################
# Create a string from the list
################################################################
# join is the inverse of split. It takes a list of strings and concatenates the elements.
# join is a string method, so you have to invoke it on the delimiter and pass

t = ['pining', 'for', 'the', 'fjords']
delimiter = ' '
s = delimiter.join(t) # 'pining for the fjords'
print(s)
























