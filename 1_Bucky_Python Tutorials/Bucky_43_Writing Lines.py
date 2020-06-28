#######################################################
# Bucky_43_Writing Lines
#######################################################

#-------------------------------------------
# Reading from the file
#-------------------------------------------
# 'read' function takes a parameter in bytes
# each character takes one byte

fob = open('C:/111/a.txt','r')

# we want to read the file as a list into the temporary variable
listme = fob.readlines()

print(listme)
# ['this is a new line \n', ' second line \n', ' third line \n']

fob.close()

#-------------------------------------------
# Let's modify the third element in the list
#-------------------------------------------
listme[2]= 'I sure love bacon \n'
print(listme)

#---------------------------------------------
# Now let's write the changed list to the file
#---------------------------------------------
fob = open('C:/111/a.txt','w')
fob.writelines(listme)

fob.close()


