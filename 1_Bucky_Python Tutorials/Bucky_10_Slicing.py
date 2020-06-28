#######################################################
# Bucky 10_Slicing
#######################################################

#---------------------------
# Slicing
#---------------------------

example = [10,17,23,38,41,57,64,73,81,98]
print(example)
print(example[4:8]) # taking 4 elemets after 4th (as it satrts counting from 0)
print(example[:7]) # taking elements from the beginning till 7th
print(example[-5:]) # starting from the fifth element from the end and take all the element till the end

print(example[:]) # all elements

print(example[0:6:2]) #taking every second element (step2)

print(example[10:0:-2]) #

print(example[::-2]) # all elements backwards with the step 2
print(example[::-1]) # all elements in the reverse order
