# implementation of card game - Memory

import simplegui
import random

global deck, exposed, state, flip1, flip2, counter, label

# helper function to initialize globals
def init():
    global deck, exposed, state, counter
    deck = range(8) + range(8)
    state = 0
    counter = 0
    label.set_text("Moves = " + str(counter))
    random.shuffle(deck)
    exposed = []
    for i in range(16):
        exposed.append(False)
     
# define event handlers
def mouseclick(pos):
    global exposed, state, flip1, flip2, deck, counter, label
    # add game state logic here
    
 
    
    length = 0
    for i in range(16):
        if ((pos[0] > (0 + length)) and (pos[0] < (50 + length))):
            #print i
            if exposed[i] == False:
                exposed[i] = True
                if state == 0:
                    state = 1
                    flip1 = i
                elif state == 1:
                    state = 2
                    flip2 = i
                    counter += 1
                    label.set_text("Moves = " + str(counter))
                else:
                    state = 1
                    if deck[flip1] != deck[flip2]:
                        exposed[flip1] = False
                        exposed[flip2] = False
                    flip1 = i
                    
        length += 50



    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global deck, exposed
    point = 0

    
    for i in range(16):
        if exposed[i] == True:
            canvas.draw_text( str(deck[i]), (15 + point, 65), 40, "Blue", "serif")
        else:
            canvas.draw_polygon([(0 + point, 0), (0 + point, 100), (50 + point, 100), (50 + point, 0)], 5, "Red", "Green")
        point += 50
    

        
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", init)
label = frame.add_label("Moves = 0")


# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()




# Always remember to review the grading rubric