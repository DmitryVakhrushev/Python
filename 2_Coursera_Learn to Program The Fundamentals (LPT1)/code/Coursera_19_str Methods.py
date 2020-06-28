#--------------------------------
# Coursera_19_str Methods
#--------------------------------

print(help(str))
print(help(str.lower))
#----------------------------

print(dir(str)) # get methods for the 'str' object

white_rabbit = "I'm late! I'm late! For a very important date!"
print(white_rabbit)

print(white_rabbit.lower()) # convert to lower case

#-------------------------------------------------
print(white_rabbit.find('late')) # returns the index of the occasion off the substring
print(white_rabbit.find('late',7)) # strating from 8th character returns the index of the occasion off the substring

print(white_rabbit.rfind('late')) # search from the end

# .find method -- returns "-1" if there is now match
print(white_rabbit.find('Late'))

#-------------------------------------------------
s = "     I'm feeling spaced out.    "
print(s.lstrip()) # remove leading spaces
print(s.rstrip()) # remove spaces at the end of the string
print(s.strip()) # remove leading and ending spaces





