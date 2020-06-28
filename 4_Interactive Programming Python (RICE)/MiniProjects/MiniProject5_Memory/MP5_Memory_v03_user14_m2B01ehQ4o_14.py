# implementation of card game - Memory

import simplegui
import random

moves = 3

num = [0,1,2,3,4,5,6,7]
random.shuffle(num)
deck = list(num)
random.shuffle(num)
deck = deck + num

print "deck = ", deck
#print "moves = ",moves

#exposed = [1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1]
exposed = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

cardIndex = 0

state = 0

card1 = 0
card2 = 0

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
    global cardIndex, state, card1, card2
        
    
    if state == 0:        
        
        state = 1
        
        card1 = pos[0]//50
        exposed[card1] = 1
        
        
        print "---------------------"
        print "state = ", state
        print "card1 index = ", card1, " value = ",deck[card1]
        print "card2 index = ", card2, " value = ",deck[card2]
        print "exposed = ", exposed
        
    
    
    elif state == 1:
    
        state = 2
        card2 = pos[0]//50
        exposed[card2] = 1
    
    
        print "---------------------"
        print "state = ", state
        print "card1 index = ", card1, " value = ",deck[card1]
        print "card2 index = ", card2, " value = ",deck[card2]
        print "exposed = ", exposed
    
    
    
    else:
        if deck[card1] != deck[card2]:
            exposed[card1] = 0
            exposed[card2] = 0
               
            state = 1
            card1 = pos[0]//50
            exposed[card1] = 1
        
            print "---------------------"
            print "state = ", state
            print "card1 index = ", card1, " value = ",deck[card1]
            print "card2 index = ", card2, " value = ",deck[card2]
            print "exposed = ", exposed
    
    
        else:
            state = 1
            card1 = pos[0]//50
            exposed[card1] = 1
    
            print "---------------------"
            print "state = ", state
            print "card1 index = ", card1, " value = ",deck[card1]
            print "card2 index = ", card2, " value = ",deck[card2]
            print "exposed = ", exposed
            

    
    
    
    
    
                        
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


    #if state == 0:
    #    canvas.draw_text("Game beginning", [30, 62], 24, "White")
    #elif state == 1:
    #    canvas.draw_text("One card exposed", [30, 62], 24, "White")
    #else:
    #    canvas.draw_text("Two cards exposed", [30, 62], 24, "White")       
        
        
                
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