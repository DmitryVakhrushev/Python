
# Py4Inf_19: Counting Words In String

#---------------------------------------------------------
# Counting Words in a String
#---------------------------------------------------------

counts = dict()

# print('Enter a line of text:')
# line = input('')
# if len(line)<=0:
#     line = 'the clown ran after the car and the car ran into the tent and the tent fell down on the clown and the car'

line = 'the clown ran after the car and the car ran into the tent and the tent fell down on the clown and the car'
print(line, '\n')

words = line.split()
print('Words:', words, '\n')

print('Counting...')
for word in words:
    counts[word] = counts.get(word, 0) + 1

print('Counts', counts)

#---------------------------------------------------------
# Printing the "KEY:VALUE" pairs from the Dictionary
#---------------------------------------------------------
print("----------------------------------------------")

for key in counts:
    print(key,counts[key])

#---------------------------------------------------------
# Printing (1) List of KEYs and (2) List of Values
#------------------------------------------------------------------------------
# The order of those two lists will correspond
print("----------------------------------------------")
print(counts.keys())
print(counts.values())


print("----------------------------------------------")
print(counts)
print("----------------------------------------------")
print(counts.items())

for aaa,bbb in counts.items():
    print(aaa, bbb)