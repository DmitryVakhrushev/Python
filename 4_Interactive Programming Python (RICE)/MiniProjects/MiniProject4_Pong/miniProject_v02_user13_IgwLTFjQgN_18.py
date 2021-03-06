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
paddle1_pos = HALF_PAD_WIDTH
paddle1_vel = 50

paddle2_pos = WIDTH - HALF_PAD_WIDTH
paddle2_vel = 300




# helper function that spawns a ball by updating the 
# ball's position vector and velocity vector
# if right is True, the ball's velocity is upper right, else upper left

def ball_init(right):
    global ball_pos, ball_vel # these are vectors stored as lists
    
    ball_vel[0] = right * int(random.randrange(120, 240)/60)
    ball_vel[1] = - int(random.randrange(60, 180)/60)
    
    print ball_vel
       
    
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
 
    # update paddle's vertical position, keep paddle on the screen
    
    global paddle1_vel, paddle2_vel
    
    if paddle1_vel + PAD_HEIGHT > HEIGHT:
        paddle1_vel = paddle1_vel
    else:
        paddle1_vel +=1
    
    paddle2_vel -=1
    
    
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # draw paddles    
        # paddle1
    c.draw_line((paddle1_pos, paddle1_vel), (paddle1_pos, paddle1_vel + PAD_HEIGHT), PAD_WIDTH, "Yellow")
        # paddle2
    c.draw_line((paddle2_pos, paddle2_vel), (paddle2_pos, paddle2_vel + PAD_HEIGHT), PAD_WIDTH, "Yellow")
    
    
    # Update ball position
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # collide and reflect off of left hand side of canvas    
    
    # check a collisiot with the LEFT wall
    if ball_pos[0] - PAD_WIDTH <= BALL_RADIUS:
        ball_vel[0] = - ball_vel[0]
    
    # check a collisiot with the RIGHT wall
    if ball_pos[0] >=(WIDTH-1 - PAD_WIDTH) - BALL_RADIUS:
        ball_vel[0] = - ball_vel[0]
    
    # check a collisiot with the TOP wall
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    
    # check a collisiot with the BOTTOM wall
    if ball_pos[1] >=(HEIGHT-1) - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    
    
    
    
    # draw ball and scores
    c.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    c.draw_text(str(score1), (230, 90), 60, "White")
    c.draw_text(str(score2), (340, 90), 60, "White")
    
def keydown(key):
    global paddle1_vel, paddle2_vel
   
def keyup(key):
    global paddle1_vel, paddle2_vel


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

start = frame.add_button("Start", new_game, 150)


# start frame
frame.start()
