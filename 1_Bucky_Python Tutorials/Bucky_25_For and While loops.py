#######################################################
# Bucky_25_For and While loops
#######################################################

#----------------------------
#------ While Loop ----------
#----------------------------
# Print in multiple rows
b = 1
while b <=10:
    print(b)
    b +=1
    
print('\n')
#----------------------------
# Print in one row
b = 1
while b <=10:
    print(b, end='')
    b +=1

print('\n')
#---------------------------
#------ For Loop -----------
#---------------------------

grocery = ['bread','milk','meat','beef']
print(grocery)

for i in grocery:
    print('I want ' + i)
    
