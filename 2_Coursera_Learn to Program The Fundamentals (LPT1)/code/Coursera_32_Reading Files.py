#-----------------------------------------
# Coursera_32_Reading Files
#-----------------------------------------

# first we need to open the file
# command --> open (filename, mode)
# mode: 'r' -- reading,  'w' -- writing, 'a' -- appending

# use the file name if it's in the same directory or the full path to the file

flanders_filename = '\\DIM\\Python\\readingFiles\\lecture_code_week6_In Flanders Fields.txt'
flanders_file = open(flanders_filename, 'r')
# readline method reads one line from the file including the end line character
line = flanders_file.readline()
while line !='':
    print(line)
    line = flanders_file.readline()

flanders_file.close()

#-------------------------------------------------
# If we do not want to print spaces between lines
#-------------------------------------------------
flanders_filename = '\\DIM\\Python\\readingFiles\\lecture_code_week6_In Flanders Fields.txt'
flanders_file = open(flanders_filename, 'r')

line = flanders_file.readline()
while line !='':
    print(line, end='')
    line = flanders_file.readline()

flanders_file.close()

#-------------------------------------------------
# Read the file till the first stanza
#-------------------------------------------------
flanders_filename = '\\DIM\\Python\\readingFiles\\lecture_code_week6_In Flanders Fields.txt'
flanders_file = open(flanders_filename, 'r')

line = flanders_file.readline()
line = flanders_file.readline()
line = flanders_file.readline()
while line !='\n':
    print(line, end='')
    line = flanders_file.readline()

flanders_file.close()

#-------------------------------------------------
# To read the whole file. Approach #1
#-------------------------------------------------
print('#-------------------------------------------------')
print('To read the whole file. Approach #1')
print('#-------------------------------------------------')

flanders_filename = '\\DIM\\Python\\readingFiles\\lecture_code_week6_In Flanders Fields.txt'
flanders_file = open(flanders_filename, 'r')

for line in flanders_file:
    print(line, end='')

flanders_file.close()

#-------------------------------------------------
# To read the whole file. Approach #2
#-------------------------------------------------
print('#-------------------------------------------------')
print('To read the whole file. Approach #2')
print('#-------------------------------------------------')

flanders_filename = '\\DIM\\Python\\readingFiles\\lecture_code_week6_In Flanders Fields.txt'
flanders_file = open(flanders_filename, 'r')

print(flanders_file.read())

flanders_file.close()

#-------------------------------------------------
# To read the whole file. Approach #3
#-------------------------------------------------
# this approach creates a list that we may want to access later

print('#-------------------------------------------------')
print('To read the whole file. Approach #3')
print('#-------------------------------------------------')

flanders_filename = '\\DIM\\Python\\readingFiles\\lecture_code_week6_In Flanders Fields.txt'
flanders_file = open(flanders_filename, 'r')

lines = flanders_file.readlines()
for x in lines:
    print(x, end='')


flanders_file.close()

print('#-------------------------------------------------')
print('Accessing the list \n')
print(lines[2], end='')
print(lines[3], end='')













