
#================================================================
# Chapter 10: Tuples
#================================================================

x = ('Glenn', 'Sally', 'Joseph')
print(x[2]) #Joseph
y = ( 1, 9, 2 )
print(y) # (1, 9, 2)
print(max(y)) # 9


# Tuples are IMMUTABLE

# dir(list)

# Much more efficient (quicker, take less memory

#-----------------------------------
t = tuple()
dir(t) # ['count', 'index']

#-----------------------------------
# Tuples and Assignment

(x, y) = (4, 'fred')
print(y) # Fred
(a, b) = (99, 98)
print(a)

#-----------------------------------
# Tuples and Dictionaries
# The items() method in dictionaries returns a list of (key, value) tuples

d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k,v) in d.items():
    print(k, v)

tups = d.items()
print(tups) # [('csev', 2), ('cwen', 4)]

#-----------------------------------
# Tuples are Comparable

# The comparison operators work with tuples and other sequences
# If the first item is equal, Python goes on to the next element,
# and so on, until it finds elements that differ.

print((0, 1, 2) < (5, 1, 2)) # True
print((0, 1, 2000000) < (0, 3, 4)) # True
print(('Jones', 'Sally' ) < ('Jones', 'Sam')) # True
print(('Jones', 'Sally') > ('Adams', 'Sam')) # True

#-----------------------------------
# Sorting Lists of  Tuples

# We can take advantage of the ability to sort a list of tuples
# to get a sorted version of a dictionary
# First we sort the dictionary by the key using the items() method

d = {'a':10, 'b':1, 'c':22}
t = sorted(d.items()) # takes a sequence as a parameter and returns a sorted sequence
print(d)
print(t) # [('a', 10), ('b', 1), ('c', 22)]

for k, v in sorted(d.items()):
    print(k, v)


#-----------------------------------
# Five most common words: sort by the value NOT by the key
# Create a temporary variable

# If we could construct a list of tuples of the form (value, key) we could sort by value
# We do this with a for loop that creates a list of tuples

c = {'a':10, 'b':1, 'c':22}
print(c)

tmp = list()
for k, v in c.items():
    tmp.append( (v, k) )

print(tmp) # [(10, 'a'), (22, 'c'), (1, 'b')]
tmp.sort(reverse=True)
print(tmp) # [(22, 'c'), (10, 'a'), (1, 'b')]


#####################################################
# The top 10 most common words (SORT a Dictionary)
#####################################################

fhand = open('romeo.txt')
# Counting words and put them into the dictionary
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0 ) + 1

# Create a list of tuples (reversing key and value from the dictionary) and sort it
lst = list()
for key, val in counts.items():
    lst.append( (val, key) )
lst.sort(reverse=True)
# Select first 10 items
for val, key in lst[:10]:
    print(key, val)

#####################################################
# Another way to sort a dictionary
#####################################################
# list Comprehension: construct dynamically a temporary list
# Create a list of tuples in the Value:Key
c = {'a':10, 'b':1, 'c':22}
print( sorted( [(v,k) for k,v in c.items()] ) ) # [(1, 'b'), (10, 'a'), (22, 'c')]


















