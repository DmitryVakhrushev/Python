# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor runs in Chrome 18+, Firefox 11+, and Safari 6+.
# Some features may work in other browsers, but do not expect
# full functionality.  It does NOT run in Internet Explorer.

import simplegui

message = "Welcome!"

# Handler for mouse click
def click():
    global message
    message = "Good job!"

# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(message, [50,112], 36, "Red")

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 200)
frame.add_button("Click me", click)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()

#--=============================================
# SimpleGUI program template

# Import the module
import simplegui

# Define global variables (program state)

# Define "helper" functions

# Define event handler functions

# Create a frame

# Register event handlers

# Start frame and timers
#--=============================================

#--=============================================
# Import the module
import simplegui

# Define global variables (program state)
counter = 0

# Define "helper" functions
def increment():
    global counter
    counter = counter + 1
    
# Define event handler functions
def tick():
    increment()
    print (counter)

def buttonpress():
    global counter
    counter = 0  

# Create a frame
frame = simplegui.create_frame("SimpleGUI Test",100,100)

# Register event handlers
timer = simplegui.create_timer(1000, tick)
frame.add_button("Click me!", tick)
frame.add_button("Another Button", buttonpress)

# Start frame and timers
frame.start()
timer.start()




