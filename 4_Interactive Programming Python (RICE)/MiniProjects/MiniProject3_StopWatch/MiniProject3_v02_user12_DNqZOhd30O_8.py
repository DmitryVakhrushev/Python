# template for "Stopwatch: The Game"

import simplegui
import time

# define global variables
curTime = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    
    minutes = str(t // 600)
    
    if ((t - (t//600)*600) // 10) < 10:
        seconds = "0" + str((t - (t//600)*600) // 10)
    else:
        seconds = str((t - (t//600)*600) // 10)
    
    millis = str(t%10)
    
    conv = minutes + ":" + seconds  + "." + millis
    return conv
       
# define event handlers for buttons; "Start", "Stop", "Reset"
def startBtn():
    tm.start()

def stopBtn():
    tm.stop()
    
def resetBtn():
    tm.stop()
    global curTime
    curTime = 0
    
# define event handler for timer with 0.1 sec interval
def tick():
    global curTime
    curTime +=1
    
# define draw handler
def drawTime(canvas):
    global curTime
    canvas.draw_text(format(curTime), (80, 120), 60, "White")
    
# create frame
f = simplegui.create_frame("Stopwatch", 300, 200)

# register event handlers
tm = simplegui.create_timer(100, tick)
f.set_draw_handler(drawTime)

start = f.add_button("Start", startBtn, 150)
stop = f.add_button("Stop", stopBtn, 150)
reset = f.add_button("Reset", resetBtn, 150)



# start frame
f.start()
tm.start()
# Please remember to review the grading rubric
