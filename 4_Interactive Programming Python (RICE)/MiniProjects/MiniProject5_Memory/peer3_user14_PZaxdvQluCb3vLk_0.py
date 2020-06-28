# implementation of card game - Memory

import simplegui
import random

cards = []
card_color = []
moves = 0

# helper function to initialize globals
def init():
    global cards, card_color, moves
    cards = range(0,8) + range(0,8)
    card_color = []
    for i in range(16):
        card_color.append("black")
    random.shuffle(cards)
    moves = 0
    
def draw_card(canvas, corner, border_color, bg_color):
    canvas.draw_polygon([(corner[0],corner[1]),
                         (corner[0],corner[1]+100),
                         (corner[0]+50,corner[1]+100),
                         (corner[0]+50,corner[1])], 
                         1, border_color, bg_color)
     
# define event handlers
def mouseclick(pos):
    global moves
    pos = pos[0] // 50
    if card_color[pos] != "black":
        return
    
    if card_color.count("blue") == 2:
        for i in range(16):
            if card_color[i] == "blue": card_color[i] = "black"
        moves += 1
    
    card_color[pos] = "blue"
    
    for i in range(16):
        if i != pos and cards[i] == cards[pos] and card_color[i] == "blue":
            card_color[i] = "green"
            card_color[pos] = "green"
            

# cards are logically 50x100 pixels in size    
def draw(canvas):
    for i in range(16):
        draw_card(canvas, [i * 50, 0], "black", card_color[i]) 
        canvas.draw_text(str(cards[i]), [50 * i + 10, 70], 64, "white")
        if card_color[i] == "black":
            draw_card(canvas, [i * 50, 0], "white", card_color[i])
    label.set_text("Moves = " + str(moves))

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