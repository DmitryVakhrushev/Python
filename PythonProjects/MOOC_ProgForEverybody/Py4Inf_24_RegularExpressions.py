
#-------------------------------------------
# Regular Expressions
#-------------------------------------------

# Really clever "wild card" expressions for matching and parsing strings.

#    ^          Matches the beginning of a line
#    $          Matches the end of the line
#    .          Matches any character
#    \s         Matches whitespace
#    \S         Matches any non-whitespace character
#    *          Repeats a character ZERO or more times
#    *?         Repeats a character ZERO or more times (non-greedy)
#    +          Repeats a character ONE or more times
#    +?         Repeats a character ONE or more times (non-greedy)
#    [aeiou]    Matches a single character IN the listed set
#    [^XYZ]     Matches a single character NOT in the listed set
#    [a-z0-9]   The set of characters can include a range
#    (          Indicates where string extraction is to START
#    )          Indicates where string extraction is to END

import re
import math

# You can use re.search()to see if a string matches
# a regular expression similar to using the find() method for strings
# You can use re.findall() extract portions of a string that match your
# regular expression similar to a combination of find() and slicing: var[5:10]

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.find('From:')>= 0:
        print(line)

print('-------------------------------------------')
import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line):
        print(line)


########################################################################
# Wild-Card Characters
########################################################################

# 1. The dot "." character matches any character
# 2. If you add the asterisk "*" character, the character is "any number of times"

print('---------- Pattern: "^X.*:" ----------')
# Match the start of the line with "X" followed by any character any number of time and then ":"
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^X.*:', line):
        print(line)

########################################################################
# \S -- Matches any non-whitespace character
# "+" -- any number of times
print('---------- Pattern: "^X-\S+:" ----------')
# This is a more specific pattern
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^X-\S+:', line):
        print(line)


print("#----------------------------------------------")
########################################################################
# Matching and Extracting Data
########################################################################

# The re.search() returns a True/False depending on whether the string matches the regular expression
# If we actually want the matching strings to be extracted, we use re.findall()

# Look for a single character (number in our case)
# [0-9]+
    # "+" means one or more digits defined in [0-9] -- between 0 and 9

# "Smart" wat to extract numbers from the string
import re
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+',x)
print(y)

z =  re.findall('[faAEIOU]+',x)
print(z)


print("#----------------------------------------------")
########################################################################
# Greedy Matching
#-----------------------------------------------------------------------
# The repeat characters (*and +) push outward in both directions (greedy) to match the largest possible string

x = 'From: Using the :character'
y = re.findall('^F.+:', x)
print(y) # ['From: Using the :'] --> it did not stop at the first ":" --> "GREEDY Match"


print("#----------------------------------------------")
########################################################################
# Non-Greedy Matching
#-----------------------------------------------------------------------

x = 'From: Using the : character'
y = re.findall('^F.+?:', x)
print(y) # ['From:'] --> ^F.+?:


print("#----------------------------------------------")
########################################################################
# Fine Tuning String Extraction
#-----------------------------------------------------------------------

# Pull an email address out of the string
x = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
y = re.findall('\S+@\S+',x)
print(y)

# Parenthesis are not part of the match - but they tell where to start and stop what string to extract
y = re.findall('^From (\S+@\S+)',x)
print(y)


# Extracting the domain name -- The Regex Version
# '@([^ ]+)' --> Look through the string until you find an at-sign
        # [^ ] --> Match non-blank character
        # + --> Match many of them at least ones
        # () extract only match in parenthesis
line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('@([^ ]+)',line)
print(y) # ['uct.ac.za']


y = re.findall('^From .*@([^ ]*)',line)
    # Starting at the beginning of the line, look for the string 'From '
    # Skip a bunch of characters, looking for an at-sign
    # () --> Start 'extracting'
print(y) # ['uct.ac.za']

######################################
# Spam Confidence
######################################
hand = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff= re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1: continue
    num = float(stuff[0])
    numlist.append(num)

print('Maximum:', max(numlist))


######################################
# Escape Character
######################################
# If you want a special regular expression character to just
# behave normally (most of the time) you prefix it with '\'

x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+',x) # Look for A real dollar sign; a digit or period
print(y)



