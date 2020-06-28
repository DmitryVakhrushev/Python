
#------------------------------------
# Reading Files
#------------------------------------

# 1.Opening a File
# 2. Read
# 3. Write
# 4. Close

# handle= open(filename, mode)
# mode = 'r' to read or = 'w' to write


fhand = open('mbox-short.txt', 'r')

# The newline Character: \n --> this a one character

stuff= 'X\nY'
print(stuff)
print("the length is = ",len(stuff)) # 3

#================================================
# Read a file LINE BY LINE
#================================================

xfile = open('mbox-short.txt')
for word in xfile:
    print(word)

#-----------------------------------
# Count the lines in the file
#-----------------------------------
fh = open('mbox-short.txt')
count = 0
for line in fh:
    count = count + 1
print('Line Count:', count)

#================================================
# READING THE ***WHOLE*** FILE --> read the whole file into a sinlge string
#================================================
# good for SMALL files as the whole file will be stored in the memory

conn1 = open('mbox-short.txt')
inp = conn1.read()
print(len(inp)) # it's a string for the whole file
print(inp[:20]) # we can slice the string

#---------------------------------
# Searching Through a File
cn2= open('mbox-short.txt')
for line in cn2:
    line = line.rstrip() # strip out "Blanks" and "New Lines" characters
    if line.startswith('From:'):
        print(line) # print itself adds "\n", so each line will be printed on the newline

print("--------------------------------------------------")

#---------------------------------
# Skipping with continue
cn3 = open('mbox-short.txt')
for line in cn3:
    line = line.rstrip()
    # skip 'uninteresting' lines
    if not line.startswith('From:'):
        continue
    print(line)
print("--------------------------------------------------")

#---------------------------------
# Using "in" to select lines
cn4 = open('mbox-short.txt')
for line in cn4:
    line = line.rstrip()
    if not '@uct.ac.za' in line:
        continue
    print(line)

#---------------------------------
# Bad File Names
fname = input('Enter the file name: ')
try:
    cn5 = open(fname)
except:
    print('File cannot be opened:', fname)
exit()
count = 0
for line in cn5:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', fname)
















