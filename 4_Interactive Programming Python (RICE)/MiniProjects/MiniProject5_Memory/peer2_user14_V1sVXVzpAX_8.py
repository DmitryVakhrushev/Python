# implementation of card game - Memory

import simplegui
import random

memorylist = []
exposed = []
state = 0
first = 0
second = 0
moves = 0

# helper function to initialize globals
def init():
    global state, first, second, moves, exposed, memorylist
    memorylist = range(8) + range(8)
    print memorylist
    exposed = []
    state = first = second = moves = 0
    random.shuffle(memorylist)
    for n in range(len(memorylist)):
        exposed.append(False)
    label.set_text("Moves = " + str(moves))    
        
# define event handlers
def mouseclick(pos):
    # add game state logic here
    # pos is the position of the mouse
    i = pos[0]//50		# i=index (0...15) in memorylist
    global state, first, second, moves
    if not exposed[i]:
        if state == 0:
           state = 1
        elif state == 1:
            state = 2
        else:
            state = 1
        if state == 1:
            moves += 1
            label.set_text("Moves = " + str(moves))
            # a first card drawn, check last pair
            if memorylist[first] == memorylist[second]:
                # matching pair
                pass
            else:
                exposed[first] = False
                exposed[second] = False
            first = i
            second = 0
        elif state == 2:
           second = i
        exposed[i] = True 
        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for n in range(len(memorylist)):
        if exposed[n]:
            canvas.draw_text(str(memorylist[n]), [(n*50 + 15), 65], 50, "White")
        else:	
            # not exposed, draw line
            canvas.draw_line((n*50, 0), ((n+1)*50 - 1, 0), 500, "Green")
            
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