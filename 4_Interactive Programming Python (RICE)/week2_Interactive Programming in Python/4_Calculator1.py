# calculator with all buttons

#-----------------------------
# 1. Import the module
#-----------------------------
import simplegui

#-----------------------------
# 2. Define global variables
#-----------------------------
store = 0
operand = 0

#-----------------------------
# 3. Define helper functions
# Functions that manipulate store and operand
#-----------------------------


#-----------------------------
# 4. event handlers for calculator with a store and operand
#-----------------------------
def output():
    print "Store = ", store
    print "Operand = ", operand
    print ""

def swap():
    global store, operand
    store, operand = operand, store
    output()

def add():
    global store, operand
    store = store + operand
    output()

def sub():
    global store, operand
    store = store - operand
    output()
    
def mult():
    """ multiply store by operand"""
    global store
    store = store * operand
    output()

def div():
    """ divide store by operand"""
    global store
    store = store / operand
    output()

def enter(inp):
    global operand
    operand = float(inp)
    output()
    
#-----------------------------
# 5. Create frame
#-----------------------------
frame = simplegui.create_frame("Calculator", 300, 300)
frame.add_button("Print", output, 100)
frame.add_button("Swap", swap, 100)
frame.add_button("Add", add, 100)
frame.add_button("Sub", sub, 100)
frame.add_button("Mult", mult, 100)
frame.add_button("Div", div, 100)

frame.add_input("Enter operand", enter, 100)

#-----------------------------
# 6. register event handlers
#-----------------------------


# 7. Start the frame
frame.start()



