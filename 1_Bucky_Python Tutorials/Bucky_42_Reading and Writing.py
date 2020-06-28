#######################################################
# Bucky_42_Reading and Writing
#######################################################

#-------------------------------------------
# Reading from the file
#-------------------------------------------
# 'read' function takes a parameter in bytes
# each character takes one byte

fob = open('C:/111/a.txt','r')
print(fob.readline())
print(fob.readlines()) # returns the file as a list
fob.close()

#-------------------------------------------
# Over writing the file info with the new data
x = open('C:/111/a.txt','w')
x.write('this is a new line \n second line \n third line \n')
# '\n' inserts a new line
x.close()


