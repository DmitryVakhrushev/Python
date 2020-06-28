#-----------------------------------------
# Coursera_35_Dictionary
#-----------------------------------------

grades = [['A',80],['A2',70],['A3',90]]
print(grades)
print(grades[0])
print(grades[1])
print(grades[2])

print(grades[1][0])
print(grades[1][1])

#-------------------------------------------
# We can use dictionary
asn_to_grade = {'A1':80, 'A2':70, 'A3':90}
print(asn_to_grade)
print(asn_to_grade['A2'])

#'A1', 'A2', and 'A3' are the keys of the dictionary
# 80, 70, 90 are the values
# !!! Keys must be UNIQUE values may be the same or different

# when we check for existence we can check keys only not values

print('A1' in asn_to_grade)
print('A4' in asn_to_grade)
print(80 in asn_to_grade) # returns FALSE even thought it's in the dictionary but as a value not as a key

# Adding a new value to the dictionary
asn_to_grade['A4'] = 85
print(asn_to_grade)

# Update a value in the dictionary
asn_to_grade['A4'] = 90
print(asn_to_grade)

# Delete a key with it's value
del asn_to_grade['A4']
print(asn_to_grade)

#-----------------------------------
# Keys may be returned in any order
for x in asn_to_grade:
    print(x)

#-----------------------------------
for x in asn_to_grade:
    print(asn_to_grade[x])

for x in asn_to_grade:
    print(x, asn_to_grade[x])

#-----------------------------------
d = {'apple':2, 5: 8}
print(d)
print(d['apple'])
print(d[5])


