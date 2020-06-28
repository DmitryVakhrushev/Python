#===============================================================================
# 04_Compare two floating point numbers.py
#===============================================================================

#------------------------------------------------------------------------------ 
# Compare two floating point numbers for equality
# as the == won't work in any language
#------------------------------------------------------------------------------ 

# Real numbers, e.g. 3.14... are infinite numbers
# and floating point numbers (in Python) are approximation of the real numbers
# basically Python rounds up those numbers at some point
# Therefore we cannot directly compare two floating point numbers as
# 6.33 = 6.33 (because 6.333333331 is not equal to 6.3333333337) 

import random

x = random.random()
xVal = int(x*10000)/100.0

y = random.random()
yVal = int(y*10000)/100.0

answer = float(input("What is the value of " + str(xVal) + "-" + str(yVal) + " equal to? "))
realAnswer =  xVal - yVal


# When you compare two floats
# 1) Substract one float from the other
# 2) Take an absolute value of the substraction
# 3) Devide by the real answer (to get the deviation from the real answer)
# 4) Compare for enaquality with some possible error, e.g. 0.01

if abs((answer - realAnswer)/realAnswer) < 0.001:
    print ("You did tit!!!")
else:
    print("No, the real answer was", realAnswer)

