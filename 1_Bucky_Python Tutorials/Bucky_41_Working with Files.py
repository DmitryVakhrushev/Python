#######################################################
# Bucky_41_Working with Files
#######################################################

#-------------------------------------------
# Writing to the file
#-------------------------------------------
fob = open('C:/111/a.txt','w') # open the connection to the file

fob.write('Hey now brown cow') # 'write' is a built in function

fob.close()

# Now we want to read the info from the file

fob = open('C:/111/a.txt','r')

#-------------------------------------------
# Reading from the file
#-------------------------------------------
# 'read' function takes a parameter in bytes
# each character takes one byte

print(fob.read(3)) # will read 3 first characters

print(fob.read()) # to read the whole file

fob.close()






