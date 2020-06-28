# template for "Stopwatch: The Game"
import simplegui

# define global variables
tick_count = 0
height = 300
width = 300
even_clicks = 0
total_clicks = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    pass
    tenths_seconds = t % 10
    seconds = (t // 10) % 10
    tens_seconds = (t // 100) % 6
    minutes = (t // 600)

    return str(minutes) + ":" + str(tens_seconds) + str(seconds) + "." + str(tenths_seconds)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_button():
    timer.start()

def stop_button():
    global tick_count, total_clicks, even_clicks

    
    if timer.is_running() == True:
        total_clicks += 1
        
    if timer.is_running() == True and tick_count % 10 == 0:
        even_clicks += 1

# stop the timer when button is pressed    
    timer.stop()
    
def reset_button():
    global tick_count, total_clicks, even_clicks
    tick_count = 0
    timer.stop()
    
    total_clicks = 0
    even_clicks = 0
    
# define event handler for timer with 0.1 sec interval
def tick():
    global tick_count
    tick_count += 1
    
# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(tick_count), (width / 2, height / 2), 25, "Red")
    canvas.draw_text(str(even_clicks) + "/" + str(total_clicks), (245, 30), 25, "Red")
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", width, height)
frame.set_draw_handler(draw_handler)
frame.add_button("Start", start_button, 200)
frame.add_button("Stop", stop_button, 200)
frame.add_button("Reset", reset_button, 200)

# register event handlers
timer = simplegui.create_timer(50, tick)

# start frame
frame.start()

# Please remember to review the grading rubric