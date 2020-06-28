#--------------------------------
# Coursera_26_Mutability and Aliasing
#--------------------------------

list1 = [1,2,3]
print(list1)
# [1, 2, 3]
list2 = list1
print(list2)
# [1, 2, 3]

list2.append(4)
print(list2)
# [1, 2, 3, 4]
print(list1)
# [1, 2, 3, 4]






