
#-------------------------------------------------------
# Assignment: 9.4
#-------------------------------------------------------

# 9.4 Write a program to read through the mbox-short.txt and figure out who has the most commits.
# The program looks for 'From ' lines and takes the second word of those lines as the person
# who sent the mail.
# The program creates a Python dictionary that maps the senders mail address
# to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary
# using a maximum loop to find the most prolific committer.

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
fh = open(name)
d = dict()
# the dictionary counts how many times each sender appeared
for line in fh:
    if line.startswith('From '):
        line = line.rstrip().split()
        d[line[1]] = d.get(line[1],0) + 1

## check the dictionary
# for kk, val in d.items():
#     print (kk,val)

# Find the maximum value in the dictionary and print this KEY-PAIR value
maxVal = 0
maxKey = ''
for dicKey in d:
    if d[dicKey] > maxVal:
        maxVal = d[dicKey]
        maxKey = dicKey

print(maxKey, d[maxKey])

