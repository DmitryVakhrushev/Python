#===============================================================================
# 4-1: Creating and Using Objects -- Kent D. Lee
#===============================================================================

import turtle

# Calling the Turtle constructor to create a Turlte Object
# Constructing a "Turtle" type using imported module "turtle"
# It's similar to creating a integer x = int('6')


t = turtle.Turtle()
# "t" is a Turtle object now
# we can print --> help('turtle') to get the documentation


t.color("#7D7EC0") # assigning a color to the line

# Mutator methods -- change the object "t"
for i in range(5):
    t.forward(200)
    t.left(144)

t.forward(200)
t.left(144)

# getscreen() is an accessor method on Turtle object
screen = t.getscreen()
screen.exitonclick()
