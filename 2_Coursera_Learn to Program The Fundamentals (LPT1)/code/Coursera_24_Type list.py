#--------------------------------
# Coursera_22_Type list
#--------------------------------
grades = [80, 90, 70]
print(grades[0])
print(grades[1])
print(grades[2])

# We can slice the list in the same way as we do with strings
print(grades[1:2])
print(grades[0:2])

# "IN" operator -- logical TRUE/FALSE
print(90 in grades)
print(60 in grades)

# Functions to apply to the list
print(len(grades))
print(min(grades))
print(max(grades))
print(sum(grades))

#----------------------------
subjects = ['bio','cs','math','history']
print(len(subjects))
print(min(subjects))
print(max(subjects))
# the sum function cannot be applied to the list of strings
#----------------------------

# Mixed string
street_address = [10, 'Main Street']
print(street_address)
print(street_address[0])
print(street_address[1])

#--------------------------------
# Loop over the list
for grade in grades:
    print(grade)

for item in subjects:
    print(item)

    






