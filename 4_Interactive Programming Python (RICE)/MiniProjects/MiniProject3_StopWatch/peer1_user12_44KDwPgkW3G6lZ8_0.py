# "Stopwatch: The Game"
import simplegui

INTERVAL = 100
TIME = 0
SCORE = [0, 0]

def format(t):
    '''(int) -> str
    Format int time variable to corresponded string
    '''
    milliseconds = t % 10
    seconds = ((t//10) % 60)
    minutes = t // 600
    return '%(minutes)d:%(seconds)02d.%(milliseconds)d' % {'minutes': minutes, 
                                                        'seconds': seconds,
                                                        'milliseconds': milliseconds}
    
def start_handler():
    '''() -> NoneType
    Handler for start button
    start the timer
    '''
    timer.start()
    
def stop_handler():
    '''() -> NoneType
    Handler for stop button
    Calculate the score according to time value
    stop the timer
    '''
    was_running = timer.is_running()
    timer.stop()
    if not was_running:
        return
    if TIME % 10:
        SCORE[1] += 1
    else:
        SCORE[0] += 1
    
def reset_handler():
    '''() -> NoneType
    Handler for reset button
    reset the game
    '''
    global TIME
    TIME = 0
    SCORE[0] = 0
    SCORE[1] = 0
    timer.stop()
    
def change_time():    
    '''() -> NoneType
    Handler for timer
    increment time
    '''
    global TIME
    TIME += 1
    
timer = simplegui.create_timer(INTERVAL, change_time)

def draw_handler(canvas):
    '''(canvas) -> NoneType
    Draw handler
    Draws time and score on
    canvas    
    '''
    canvas.draw_text(format(TIME), (90, 120), 42, "Red")
    canvas.draw_text('%i/%i' % (SCORE[0], SCORE[1]),
                     (180, 60), 24, "GREEN")
    
frame = simplegui.create_frame("Stopwatch: The Game", 300, 200)

frame.add_button("Start", start_handler, 100)
frame.add_button("Stop", stop_handler, 100)
frame.add_button("Reset", reset_handler, 100)
frame.set_draw_handler(draw_handler)

frame.start()