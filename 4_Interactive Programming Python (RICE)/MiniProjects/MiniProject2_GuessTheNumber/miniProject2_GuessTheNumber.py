
#-------------------------------------------------
# Mini Project #2 -- Guess the Number
#-------------------------------------------------


# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console


#-------------------------------------------------
# initialize global variables used in your code


# define event handlers for control panel
    
def range100():
    # button that changes range to range [0,100) and restarts

def range1000():
    # button that changes range to range [0,1000) and restarts
    
def get_input(guess):
    # main game logic goes here    

    
# create frame


# register event handlers for control elements


# start frame


# always remember to check your completed program against the grading rubric

----------------


#-------------------------------------------------
# Mini Project #2 -- Guess the Number
#-------------------------------------------------


# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console


#-------------------------------------------------

import simplegui
import random

# initialize global variables used in your code

compNumber = -1
attempts = 0

# define event handlers for control panel
    
def range100():
    # button that changes range to range [0,100) and restarts
    print "Range (0 - 100) was selected"
    print "Computer has chosen a number. Please guess!"
    global compNumber, counter
    compNumber = random.randint(0, 99)
    counter = 7
    print "Secret number is " + str(compNumber)
    print "Counter = " + str(counter)
    print ""
    
    
def range1000():
    # button that changes range to range [0,1000) and restarts
    print "Range (0 - 1000) was selected"
    print "Computer has chosen a number. Please guess!"
    global compNumber, counter
    counter = 10
    compNumber = random.randint(0, 999)
    
    print "Secret number is " + str(compNumber)
    print "Counter = " + str(counter)
    
def get_input(guess):
    # main game logic goes here    
    global compNumber, counter
    
    if compNumber == -1:
        print "*******************************"
        print "****** Select a range *********"
        print "*******************************"
        print ""
    
    if guess == "": guess = -1
    if int(guess) < compNumber and compNumber != -1:
        print "Guess was " + guess
        counter -=1
        if counter > 0:
            print "Number of remaining guesses " + str(counter)
            print "Higher!"
            print ""
        else:
            print "You ran out of guesses. The number was " + str(compNumber)
            print ""
            compNumber = -1
            
    elif int(guess) > compNumber and compNumber != -1:
        print "Guess was " + guess
        counter -=1
        print "Number of remaining guesses " + str(counter)
        print "Lower!"
        print ""
    
    
    if int(guess) == compNumber and compNumber != -1:
        print "Correct!!!"
        print ""
        
    
# create frame
f = simplegui.create_frame("Guess the number", 300, 200)


# register event handlers for control elements
f.add_button("Range: 0 - 100", range100, 200)
f.add_button("Range: 0 - 1000", range1000, 200)

f.add_input("Enter your guess", get_input, 200)


# start frame
f.start()
range100()

# always remember to check your completed program against the grading rubric