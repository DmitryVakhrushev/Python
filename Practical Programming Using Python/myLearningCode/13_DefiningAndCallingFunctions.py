#===============================================================================
# 5-1: Defining and Calling Functions -- Kent D.Lee
#===============================================================================

import turtle

# define a function doesn't mean it's execution

def f(x):
    return x*x*x # cube of x

t = turtle.Turtle()
screen = t.getscreen()
screen.setworldcoordinates(-10,-10,10,10)

t.penup()
t.goto(-20, -20)
t.pendown()

for k in range(-30, 30, 1):
    myX = k/10
    myY = f(myX)
    t.goto(myX, myY)

screen.exitonclick()



