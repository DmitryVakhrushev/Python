import math


#------------------------------------
# Function #1

def area(base, height):
    '''
    (number, number) -> number

    Return the area of the triangle with dimensions base
    and height
    '''
    return base*height/2


#------------------------------------
# Function #2

def perimeter(side1, side2, side3):
    '''(number, number, number) -> number

    Return the perimeter of a triangle with sides of length
    side1, side2 and side3.

    >>> perimeter(3, 4, 5)
    12
    >>> perimeter(10.5, 6, 9.3)
    25.8
    '''
    return side1 + side2 + side3

#------------------------------------
# Function #3

def semiperimeter(side1, side2, side3):
    '''(number, number, number) -> float

    Return the semiperimeter of a triangle with sides of
    lemgth side1, side2, side3.
    
    >>> semiperimeter(3,4,5)
    6.0
    >>> semiperimeter(10.5, 6, 9.3)
    12.9
    '''
    return perimeter(side1, side2, side3)/2


#------------------------------------
# Function #4

def area_hero(side1, side2, side3):

    ''' (number, number, number) -> float

    Returns the area of a triangle with sides of lenth
    side1, side2, and side3.

    >>> area_hero(3,4,5)
    6.0
    >>> area_hero(10.5,6,9.3)
    27.731
    '''
    semi = semiperimeter(side1, side2, side3)
    area = math.sqrt(semi*(semi-side1)*(semi-side2)*(semi-side3))
    return area


#########------------------------------------
# We can also import modules that we wrote.
# This file has to be in the same directory as the file that calls it.
# To call it you have to mention the:
#             (1) module name and
#             (2) the function name in this module

import Coursera_02_temperature_convertor
print(Coursera_02_temperature_convertor.convert_to_celsius(238))




