# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# initialize global variables used in your code
secret_num = 0
num_trials = 7

# define event handlers for control panel
    
def range100():
    # button that changes range to range [0,100) and restarts
    global secret_num, num_trials
    num_trials = 7
    secret_num = random.randrange(0,100)
    print "New game. Range is from 0 to 100"
    print "Number of remaining guesses is 7"
    print ""
    
def range1000():
    # button that changes range to range [0,1000) and restarts
    global secret_num, num_trials
    num_trials = 10
    secret_num = random.randrange(0,1000)
    print "New game. Range is from 0 to 1000"
    print "Number of remaining guesses is 10"
    print ""
    
def get_input(guess):
    # main game logic goes here	
    global secret_num, num_trials
    num_trials -= 1
    print "Guess was", guess
    print "Number of remaining guesses is", num_trials
    g = int(guess)
    if g < secret_num:
        print "Higher!"
        print ""
        if num_trials == 0:
            print "You lose"
            print ""
            range100()
    elif g > secret_num:
        print "Lower!"
        print ""
        if num_trials == 0:
            print "You lose"
            print ""
            range100()
    elif g == secret_num:
        print "Correct!"
        print ""
        range100()
   
    
# create frame
frame = simplegui.create_frame("Guess the number",200,200)

# register event handlers for control elements
frame.add_button("Range [0,100)", range100, 200)
frame.add_button("Range [0,1000)", range1000, 200)
frame.add_input("Enter your guess", get_input, 200)

# start frame
frame.start()
range100()
# always remember to check your completed program against the grading rubric
