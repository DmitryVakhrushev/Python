#-------------------------------------
# Quiz 1
#-------------------------------------

# not (p or not q)

print (not (True or not True))
print not (True or not False)
print not (False or not True)
print not (False or not False)

print "-------- n = 123.4 ---------------------"
n = 123.4
print (n / 10) % 10
print ((n - n % 10) % 100) / 10 
print (n % 100 - n % 10) / 10 

print "-----------------------------"
n = 75.1
print ((n - n % 10) % 100) / 10 
print (n % 10) / 10
print (n // 10) % 10

print "-----------------------------"

import random

print float(random.randint(0, 10))
print float(random.randrange(0, 10))


print "-------f(x) = -5 x5 + 69 x2 - 47 -----------"
# f(x) = -5 x5 + 69 x2 - 47 
def eq(x):
    y = -5*x**5 + 69*x**2 - 47
    return y

print eq(0)
print eq(1)
print eq(2)
print eq(3)

print "-----------------------------"
def future_value(present_value, annual_rate, periods_per_year, years):
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years
    
    fv = present_value*(1+rate_per_period)**periods
    return fv
    
    # Put your code here.

print "$1000 at 2% compounded daily for 3 years yields $", future_value(1000, .02, 365, 3)

print future_value(500, .04, 10, 10)

print "-----------------------------"
# Function that calculates the area of a regular polygon

import math

def polarea(nsides, side_length):
    area = 1/4 * nsides * side_length**2 / math.tan(math.pi/nsides)
    return area

print polarea(5,7)
print polarea(7,3)

print "-----------------------------"
def project_to_distance(point_x, point_y, distance):
    dist_to_origin = math.sqrt(point_x ** 2 + point_y ** 2)
    scale = distance / dist_to_origin
    print point_x * scale, point_y * scale
    
project_to_distance(2, 7, 4)







