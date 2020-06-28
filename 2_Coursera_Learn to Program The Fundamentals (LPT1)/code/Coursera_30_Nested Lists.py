#-----------------------------------------
# Coursera_30_Nested Lists
#-----------------------------------------
grades = [['Assignment 1', 80], ['Assignment 1', 90],['Assignment 1', 70]]
print(grades)

print(grades[0])
# ['Assignment 1', 80]
print(grades[1])
# ['Assignment 1', 90]
print(grades[2])
# ['Assignment 1', 70]

print(len(grades[0]))
# 2

for item in grades:
    print(item)
# ['Assignment 1', 80]
# ['Assignment 1', 90]
# ['Assignment 1', 70]

# we can access each element in the nested list
print(grades[0][0])
print(grades[0][1])

print(grades[1][0])
print(grades[1][1])

# Calculate the AVG of grades
def calculate_average(asn_grades):
    '''(list of list of [str, number]) -> float
    Return the average of the grades in asn_grades.
    >>> calculate_average([['A1',80],['A2',90]])
    85.0
    '''
    total = 0
    for item in asn_grades:
        total = total + item[1]

    return total/len(asn_grades)


