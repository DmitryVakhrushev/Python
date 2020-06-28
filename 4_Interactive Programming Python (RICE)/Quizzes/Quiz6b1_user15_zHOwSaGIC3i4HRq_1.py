CARD_SIZE = (73,98)
CARD_CENTER = (36.5, 49)

i = 12
j = 3

card_pos = [CARD_CENTER[0] + i * CARD_SIZE[0],
CARD_CENTER[1] + j * CARD_SIZE[1]]

print card_pos[0], card_pos[1]

#-----------------------
def list_extend_many(lists):
    """Returns a list that is the concatenation of all the lists in the given list-of-lists."""
    result = []
    for l in lists:
        result.extend(l)
    return result

print list_extend_many([[1,2], [3], [4, 5, 6], [7]])

print "---------------------"

def list_extend_many(lists):
    result = []
    while len(lists) > 0:
        result.extend(lists.pop(0))
    return result

print list_extend_many([[1,2], [3], [4, 5, 6], [7]])


################################
def list_extend_many(lists):
    result = []
    for i in range(len(lists) - 1, -1, -1):
        result.extend(lists[i])
    return result

print list_extend_many([[1,2], [3], [4, 5, 6], [7]])

###############
def list_extend_many(lists):
    result = []
    i = 0
    while i < len(lists): 
        result.extend(lists[i])
        i += 1
    return result

print list_extend_many([[1,2], [3], [4, 5, 6], [7]])

######################################
def list_extend_many(lists):
    result = []
    i = 0
    while i < len(lists): 
        result += lists[i]
        i += 1
    return result

print list_extend_many([[1,2], [3], [4, 5, 6], [7]])

#-----------------------------
print "----------------------"
#n = 10
#num = [2,3,4,5,6,7,8,9]
num = range(2, 1000)
result = []
copyNum = []
x = 0

while len(num) > 0:
    result.append(num[0])
    for i in num:
        if i % result[x] !=0:
            copyNum.append(i)
    num = list(copyNum)
    x +=1
    copyNum = []

#result.append(number[0])
# print result
print len(result)


#---------------------------------
print "---------------------------"
slow = 1000
fast = 1
year = 1

#while slow > fast:
for i in range (1,45):
    #print i
    slow = (slow + slow)*0.6
    fast = (fast + fast)*0.7
    #print "slow = ", slow
    #print "fast = ", fast
    year +=1

print "slow = ", slow
print "fast = ", fast
print "year = ", year




    













