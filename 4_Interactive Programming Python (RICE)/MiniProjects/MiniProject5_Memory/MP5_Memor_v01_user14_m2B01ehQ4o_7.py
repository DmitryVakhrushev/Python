# implementation of card game - Memory

import simplegui
import random

moves = 3

num = [0,1,2,3,4,5,6,7]
random.shuffle(num)
deck = list(num)
random.shuffle(num)
deck = deck + num

print deck
print moves

exposed = [1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1]
#exposed = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

# helper function to initialize globals
def init():
    global moves
    moves = 35
    label.set_text("Moves = " + str(moves))
    random.shuffle(deck)
    
    print deck
    
    
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    pass
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    numPosition = 10
    linePos = 25
    for i in range(len(deck)):
        if deck[i] != deck[i] + exposed[i]:
            canvas.draw_text(str(deck[i]), (numPosition, 70), 50, "White")
        else:
            canvas.draw_line((linePos, 0), (linePos, 100), 48, "Green")
            
        numPosition += 50
        linePos +=50


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", init)
label = frame.add_label("Moves = 0")



# initialize global variables
#init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()


# Always remember to review the grading rubric