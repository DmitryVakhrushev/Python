# Week 2
# Function Reuse
# Calling functions within other function definitions


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
    
