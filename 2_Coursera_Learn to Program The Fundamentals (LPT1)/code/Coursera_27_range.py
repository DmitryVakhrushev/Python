#--------------------------------
# Coursera_27_range
#--------------------------------

for num in range(10):
    print(num)

'''
>>> help(range)
Help on class range in module builtins:

class range(object)
 |  range([start,] stop[, step]) -> range object

'''

s = 'computer science'
print(len(s))
for i in range(len(s)):
    print(i)

# starting from index 1
for i in range (1, len(s)):
    print(i)

# printing odd indexes
for i in range(1, len(s), 2):
    print(i)




