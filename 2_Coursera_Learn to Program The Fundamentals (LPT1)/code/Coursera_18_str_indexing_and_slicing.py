
# Coursera_18_str_indexing_and_slicing.py

s = 'Learn to Program'

#---------------------------------------------
# Indexing --> getting one character at a time
print(s[0]) # indexing
print(s[1])
print(s[2])

print(s[0]) # indexing from the end
print(s[-1])
print(s[-2])
print(s[-3])

#---------------------------------------------
# Slicing
print(s[0:5]) # from 0 to NOT including 5
print(s[6:8])
print(s[9:16])

print(s[9:len(s)])

print(s[9:])
print(s[:8])
print(s[:])

print(s[1:8])
print(s[1:-8])
print(s[-15:-8])

#---------------------------------------------
# If we want to modify the string
s = s[:5] + 'ed' + s[5:]
print(s)





