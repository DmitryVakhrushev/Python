
#-------------------------------------
# week1_Lecture6_Programming Tips
#-------------------------------------

############
# This is a compilation of the examples from Week 1's Programming Tips.
# Many of these functions have errors, so this file won't run as is.
############


import math

############
# Has multiple NameErrors
def volume_cube(side):
    return side ** 3

s = 2
# print ("Volume of cube with side", s, "is", volume(s), ".")


############
# Has a NameError

import random

def random_dice():
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    return die1 + die2

print ("Sum of two random dice, rolled once:", random_dice())
print ("Sum of two random dice, rolled again:", random_dice())
print ("Sum of two random dice, rolled again:", random_dice())


############
# Has an AttributeError
def volume_sphere(radius):
    return 4/3 * math.pi * (radius ** 3)

r = 2
print ("Volume of sphere of radius", r, "is", volume_sphere(r), ".")


############
# Has multiple TypeErrors
def area_triangle(base, height):
    return 1/2 * base * height

b = 5
h = 2 + 2
print ("Area of triangle with base", b, "and height", h, "is", area_triangle(b,h), ".")


############
# Has multiple SyntaxErrors
def is_mary(x):
    if x == "Mary":
        print ("Found Mary!")
    else:
        print ("No Mary.")

is_mary('Mary')
is_mary('Fred')


############
# Poor readability
def area_triangle_sss(side1, side2, side3):
    '''Return the area of the triangle given the lenghts
    of its three sides.
    '''
    # Uses Heron's formula
    semi_perim = (side1 + side2 + side3)/2
    return math.sqrt(semi_perim *
                     (semi_perim - side1)*
                     (semi_perim - side2)*
                     (semi_perim - side3))

base = 3
height = 4
hyp = 5
print ("Area of triangle with sides", base, height, hyp, "is", area_triangle_sss(base, height, hyp), ".")


############
# Could use error-checking of input value
def favorites(instructor):
    """Returns the favorite thing of the given instructor."""
    
    if instructor == "Joe":
        return "games"
    elif instructor == "Scott":
        return "ties"
    elif instructor == "John":
        return "outdoors"
    
    else:
        print('Favorite saw invalid instructor', instructor) 
print (favorites("John"))
print (favorites("Jeannie"))









