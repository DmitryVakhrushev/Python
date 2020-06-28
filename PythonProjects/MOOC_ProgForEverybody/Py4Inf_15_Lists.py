
#----------------------------------------------
# Python Lists -- Chapter 8
#----------------------------------------------

# To convert from a string to a list of characters, you can use list:
s = 'spam'
t = list(s)
print(t) # ['s', 'p', 'a', 'm']

# A Listis a kind of Collection

friends = ['Joseph', 'Glenn', 'Sally']
carryon = ['socks', 'shirt', 'perfume']

# List constants are surrounded by square brakets and the elements in the list are separated by commas
# A listelement can be any Python object - even another list
# A listcan be empty

print([1, 24, 76])
print(['red', 'yellow', 'blue'])
print(['red', 24, 98.6])
print([ 1, [5, 6], 7])
print([])

x = [1,2,'joe',99]
print(len(x))

# RANGE function
# "range" function produces a list and gives it back to us

print(range(4))

# Iterating over lists

people = ['Joseph', 'Glenn', 'Sally']

# For loop to loop through the list
for per in people:
    print(per)

# Another way to write the sanme loop
for i in range(len(people)):
    print(people[i])


# Concatenatinglists using "+"
a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)

#----------------------------------------------------------------
# List Methods
#----------------------------------------------------------------
z = []
print(type(z))
print(dir(z))
# 'append', 'clear', 'copy', 'count', 'extend',
# 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

stuff = list() # or we can say stuff = []
stuff.append('book')
stuff.append(99)
print(stuff)
stuff.append('cookie')
print(stuff) # ['book', 99, 'cookie']

x1 = [9,13,1,88,7]
print(x1)
x1.sort() # this method changes the list (the order)
print(x1)

#---------------------------------------------------
# Is Something in a List?
some = [1, 9, 21, 10, 16]
print(9 in some) # True
print(15 in some) # False
print(20 not in some) # True

#---------------------------------------------------
# Built in Functions and Lists
# https://docs.python.org/3/library/functions.html?highlight=built%20functions
nums = [3, 41, 12, 9, 74, 15]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))

##############################
# total = 0
# count = 0
# while True :
#     inp = input('Enter a number: ')
#     if inp == 'done' : break
#     value = float(inp)
#     total = total + value
#     count = count + 1
#
# average = total / count
# print('Average:', average)
#
# # Another variant of the same program using lists
# numlist = list()
# while True :
#     inp = input('Enter a number: ')
#     if inp == 'done' : break
#     value = float(inp)
#     numlist.append(value)
#
# average = sum(numlist) / len(numlist)
# print('Average:', average)

#---------------------------------------------------
# Best Friends: Strings and Lists
# Splitbreaks a string into parts produces a list of strings.

abc = 'With three words'
stuff = abc.split()
print(stuff) # ['With', 'three', 'words']
print(len(stuff))
print(stuff[0])


line ='A lot of spaces'
etc = line.split()
print(etc) # ['A', 'lot', 'of', 'spaces']

#--------------------------------------------
# Specify a delimeter
#--------------------------------------------
line ='first;second;third'
thing = line.split()
print(thing) #['first;second;third']
print(len(thing))

thing = line.split(';')
print(thing) # ['first', 'second', 'third']
print(len(thing))


###########################################################
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    print(words[2])

#+++++++++++++++++++++++++++++++++++++
# The Double Split Pattern
# Sometimes we split a line one way and then grab one of the pieces of
# the line and split that piece again

line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
words = line.split()
email = words[1]
pieces = email.split('@')
print(pieces)
print(pieces[1])













