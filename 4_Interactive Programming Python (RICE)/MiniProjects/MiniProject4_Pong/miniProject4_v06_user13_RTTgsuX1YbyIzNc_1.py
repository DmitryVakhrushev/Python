# Implementation of classic arcade game Pong

import simplegui
import random
import math

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2

score1 = 0
score2 = 0

ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0, 0]

# paddles
paddle1_pos = 150
paddle1_vel = 0

paddle2_pos = 150
paddle2_vel = 0


# helper function that spawns a ball by updating the 
# ball's position vector and velocity vector
# if right is True, the ball's velocity is upper right, else upper left

def ball_init(right):
    global ball_pos, ball_vel # these are vectors stored as lists
    
    ball_vel[0] = right * int(random.randrange(120, 240)/60)
    ball_vel[1] = - int(random.randrange(60, 180)/60)
       
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats
    
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    
    direction = random.choice([-1,1])        
    ball_init(direction)
    
    
def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel  
    global paddle1_vel, paddle2_vel
    
    # update paddle's vertical position, keep paddle on the screen
    
    paddle1_pos += paddle1_vel
    
    if paddle1_pos <= 0: paddle1_pos = 0
    elif paddle1_pos > 320: paddle1_pos = 320
    else: paddle1_pos += paddle1_vel

        
    paddle2_pos += paddle2_vel        
        
    if paddle2_pos <= 0: paddle2_pos = 0
    elif paddle2_pos > 320: paddle2_pos = 320
    else: paddle2_pos += paddle2_vel
    
    
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # draw paddles    
    # paddle1
    c.draw_line((HALF_PAD_WIDTH+1, paddle1_pos), (HALF_PAD_WIDTH+1, paddle1_pos + PAD_HEIGHT), PAD_WIDTH, "Red")
    
    # paddle2
    c.draw_line((WIDTH - HALF_PAD_WIDTH, paddle2_pos), (WIDTH - HALF_PAD_WIDTH, paddle2_pos + PAD_HEIGHT), PAD_WIDTH, "Yellow")
    
    # Update ball position    
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
#---------------------------------------------------------
    # collide and reflect off of left hand side of canvas    
    # check colission with paddle1
    
    # Check collision with LEFT paddle
    if ball_pos[0] <= (PAD_WIDTH + BALL_RADIUS + 4) and (ball_pos[1] >= paddle1_pos and ball_pos[1] <= paddle1_pos + PAD_HEIGHT):
        ball_pos[0] = 30
        ball_vel[0] = - ball_vel[0]*1.1
    
    # Check collision with Right paddle
    if ball_pos[0] >= (WIDTH-5 - PAD_WIDTH - BALL_RADIUS) and (ball_pos[1] >= paddle2_pos and ball_pos[1] <= paddle2_pos + PAD_HEIGHT):
        ball_pos[0] = 570
        ball_vel[0] = - ball_vel[0]*1.1
    
    # Check collision with the LEFT gutter
    if ball_pos[0] - PAD_WIDTH <= BALL_RADIUS:        
        score2 += 1
        ball_pos[0] = WIDTH / 2
               
        ball_vel[0] =  int(random.randrange(120, 240)/60)
        ball_vel[1] = - int(random.randrange(60, 180)/60)
                  
    # Check collision with the RIGHT gutter
    if ball_pos[0] >=(WIDTH-1 - PAD_WIDTH) - BALL_RADIUS:        
        score1 += 1
        ball_pos[0] = WIDTH / 2
        ball_vel[0] = - random.randrange(120, 240)/60
        ball_vel[1] = - random.randrange(60, 180)/60
    
    # check a collision with the TOP wall
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    
    # check a collision with the BOTTOM wall
    if ball_pos[1] >=(HEIGHT-1) - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]

#---------------------------------------------------------    
    # draw ball and scores
    c.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    c.draw_text(str(score1), (230, 90), 60, "White")
    c.draw_text(str(score2), (340, 90), 60, "White")
#---------------------------------------------------------

#**************************  
# Key PRESSED UP
def keyup(key):
    global paddle1_vel, paddle2_vel
    
# paddle1
    if chr(key) in "WS":
       paddle1_vel = 0
       #print paddle1_vel
    
# paddle2
    if chr(key) in "(&":
       paddle2_vel = 0
       #print paddle2_vel

# Key PRESSED DOWN  
def keydown(key):
    global paddle1_vel, paddle2_vel
    
# paddle1
    if chr(key) in "W":
        paddle1_vel = -5
        #print paddle1_vel 

    if chr(key) in "S":
        paddle1_vel = 5
        #print paddle1_vel
      
# paddle2        
    if chr(key) in "&":
        paddle2_vel = -5
        #print paddle2_vel 

    if chr(key) in "(":
        paddle2_vel = 5
        #print paddle2_vel
   
#---------------------------------------------------------
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

start = frame.add_button("Restart", new_game, 150)

# start frame
frame.start()
