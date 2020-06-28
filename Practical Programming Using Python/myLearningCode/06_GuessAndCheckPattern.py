
#------------------------------------
# Kent D. Lee lesson on YoutTube
# 2-1: The Guess and Check Pattern 
#------------------------------------

x = int(input("Please enter the 1st integer: "))
y = int(input("Please enter the 2nd integer: "))
z = int(input("Please enter the 3rd integer: "))

# Make a guess
maxVal = x

# Fix my guess
if maxVal < y:
    maxVal = y

# Fix my guess    
if maxVal < z:
    maxVal = z

print ("The maximum number is ", maxVal)    


