# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
    


# helper function that spawns a ball by updating the 
# ball's position vector and velocity vector
# if right is True, the ball's velocity is upper right, else upper left
def ball_init(right):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]
    # add randomization to the velocity
    if (right):
        ball_vel = [random.randrange(120,240)/60, - random.randrange(60,180)/60]
    else:
        ball_vel = [- random.randrange(120,240)/60, - random.randrange(60,180)/60]

    
# define event handlers

def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats
    global score1, score2  # these are ints
    paddle1_pos = [0,(HEIGHT/2) - HALF_PAD_HEIGHT]
    paddle2_pos = [(WIDTH - PAD_WIDTH), (HEIGHT/2) - HALF_PAD_HEIGHT]
    
    paddle1_vel = [0,0]
    paddle2_vel = [0,0]
    
    score1 = 0
    score2 = 0
    
    ball_init(1)
    
def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
    # update paddle's vertical position, keep paddle on the screen
    if ((paddle1_pos[1] <= 0) and (paddle1_vel[1] <0) ):
        print "cannot go up position anymore"
    elif ((paddle1_pos[1] >= (HEIGHT - PAD_HEIGHT)) and (paddle1_vel[1] >0)):    
        print "cannot go down anymore"
    else:
        paddle1_pos[1] += paddle1_vel[1]
        
    if ((paddle2_pos[1] <= 0) and (paddle2_vel[1] < 0)):
        print "cannot go up anymore"
    elif ((paddle2_pos[1] >= (HEIGHT - PAD_HEIGHT)) and (paddle2_vel[1] > 0)):   
        print "cannot go down anymore"
    else:
        paddle2_pos[1] += paddle2_vel[1]
    
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # draw paddles
    c.draw_polygon([(paddle1_pos[0], paddle1_pos[1]), (PAD_WIDTH, paddle1_pos[1]), (PAD_WIDTH, (paddle1_pos[1] + PAD_HEIGHT)), (0, (paddle1_pos[1] + PAD_HEIGHT))],1,"White","White")
    c.draw_polygon([(paddle2_pos[0], paddle2_pos[1]), (WIDTH, paddle2_pos[1]), ((WIDTH + PAD_WIDTH), (paddle2_pos[1] + PAD_HEIGHT)), ((WIDTH - PAD_WIDTH), (paddle2_pos[1] + PAD_HEIGHT))],1,"White","White")
    
    # update ball position
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    #collide and reflect
    if ball_pos[1] >= (HEIGHT - BALL_RADIUS):
        ball_vel[1] = - ball_vel[1]
    elif ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    
    if (ball_pos[0] <= (PAD_WIDTH + BALL_RADIUS)):
        if (((ball_pos[1]) >= (paddle1_pos[1])) and (ball_pos[1] <= ((paddle1_pos[1]) + PAD_HEIGHT))):
            print "strike"
            ball_vel[0] = (- ball_vel[0] ) - (0.1 * ball_vel[0])
        else:
            print "paddle1 missed"
            score2 += 1
            ball_init(1)
    elif (ball_pos[0] >= (WIDTH -(PAD_WIDTH + BALL_RADIUS))):
        if (((ball_pos[1]) >= (paddle2_pos[1])) and (ball_pos[1] <= ((paddle2_pos[1]) + PAD_HEIGHT))):
            print "strike"
            ball_vel[0] = (- ball_vel[0]) - (0.1 * ball_vel[0])
        else:
            print "paddle2 missed"
            score1 += 1
            ball_init(0)

    # draw ball and scores
    c.draw_circle(ball_pos,BALL_RADIUS,2,"Red","White")
    c.draw_text("SCORE="+str(score1),(70,50),20,"White")
    c.draw_text("SCORE="+str(score2),(400,50),20,"White")
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel[1] = -3
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel[1] = 3
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel[1] = -3
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel[1] = 3
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel[1] = 0
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel[1] = 0
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel[1] = 0
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel[1] = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
new_game()
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart",new_game,70)

# start frame
frame.start()
