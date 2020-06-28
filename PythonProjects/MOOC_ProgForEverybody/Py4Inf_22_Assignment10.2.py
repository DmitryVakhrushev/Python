
#------------------------------------------------------
# Assignment 10.2
#------------------------------------------------------

# Write a program to read through the mbox-short.txt
# and figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line
# by finding the time and then splitting the string a second time using a colon.

# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

# Once you have accumulated the counts for each hour,
# print out the counts, sorted by hour as shown below.
# Note that the autograder does not have support for the sorted() function.

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"

try:
    handle = open(name,'r')
except:
    print ('File "{}" is not found:'.format(name))
    exit()

# create a dictionary that counts number of messages for each hour
time = list()
hour = list()
d = dict()
for line in handle:
    if line.startswith('From '):
        #print(line.rstrip())
        time = line.rstrip().split()[5]
        hour = time.split(':')[0]
        d[hour] = d.get(hour,0) + 1
        #break

# Create a sorted list: sorting by hour
lst = list()
for key, value in d.items():
    lst.append((key,value))
    lst.sort()

# printing out the pairs of "Hour: Number of Messages"
for key, value in lst:
    print(key, value)
