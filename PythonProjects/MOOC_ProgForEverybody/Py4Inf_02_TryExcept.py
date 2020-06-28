#-------------------------------------------------------------
# The try/ except Structure
#-------------------------------------------------------------

# Chapter #3

# You surround a dangerous section of code with tryand except
# If the code in the "try" works - the "except" is skipped
# If the code in the "try" fails - it jumps to the "except" section

# It doesn't interrupt the program if an error occurs
# When "traceback" happens Python stops executing
# if there are multiple lines in the TRY block it runs till one dies
#----------
astr = 'Hello Bob'
try:
    istr = int(astr)
except:
    istr = -1
print ('First', istr)


#----------
astr = '123'
try:
    istr = int(astr)
except:
    istr = -2
print('Second', istr)

#----------
astr = 'Hello Bob'
try:
    print('Hello')
    istr = int(astr)
    print('Bob')
except:
    istr = -3
print ('Done', istr)