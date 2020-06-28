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
right = random.randrange(0, 2)
score1 = 0
score2 = 0



# helper function that spawns a ball by updating the 
# ball's position vector and velocity vector
# if right is True, the ball's velocity is upper right, else upper left


def ball_init(right):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    width_speed = random.randrange(120 / 60, 240 / 60)
    height_speed = -(random.randrange(60 / 60, 180 / 60))
    if right == True:
        ball_vel = [width_speed , height_speed]
    if right == False:
        ball_vel = [- width_speed, height_speed]

# define event handlers

def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats
    global score1, score2  # these are ints
    ball_init(right)
    paddle1_pos = HEIGHT / 2
    paddle2_pos = HEIGHT / 2
    paddle1_vel = 0
    paddle2_vel = 0
    score1 = int(score1)
    score2 = int(score2)
    score1 = 0
    score2 = 0

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    
    
    # update paddle's vertical position, keep paddle on the screen
    #pad pos check
    if 0 > paddle1_pos:
        paddle1_pos = 0
    if paddle1_pos > (HEIGHT - PAD_HEIGHT):
        paddle1_pos = HEIGHT - PAD_HEIGHT
    if 0 > paddle2_pos:
        paddle2_pos = 0
    if paddle2_pos > HEIGHT - PAD_HEIGHT:
        paddle2_pos = HEIGHT - PAD_HEIGHT
        
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel
        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # draw paddles
    #paddle 1
    c.draw_polygon([[PAD_WIDTH,0 + paddle1_pos],[0, 0 + paddle1_pos], [0, PAD_HEIGHT + paddle1_pos], [PAD_WIDTH, PAD_HEIGHT + paddle1_pos]], 1, "White", "White")
    c.draw_polygon([[600 ,0 + paddle2_pos], [600 - PAD_WIDTH, 0 + paddle2_pos], [600 - PAD_WIDTH, PAD_HEIGHT + paddle2_pos], [600, PAD_HEIGHT + paddle2_pos]], 1, "White", "White") 
    # update ball
        # collide and reflect off of left hand side of canvas
        # gauche
    if ball_pos[0] <= (BALL_RADIUS + PAD_WIDTH):
        ball_vel[0] = - ball_vel[0]
        #bas
    if ball_pos[1] <= (HEIGHT - BALL_RADIUS):
           ball_vel[1] = - ball_vel[1]
        #droite
    if ball_pos[0] >= (WIDTH - (PAD_WIDTH + BALL_RADIUS)):
          ball_vel[0] = - ball_vel[0]
        #haut
    if ball_pos[1] >= (BALL_RADIUS) :
          ball_vel[1] = - ball_vel[1]
            
     # restart if touch the gutter
        # gauche    
    if ball_pos[0] <= (BALL_RADIUS + PAD_WIDTH) and not(paddle1_pos <= ball_pos[1] <= paddle1_pos + PAD_HEIGHT):
       ball_init(True)
       score2 = int(score2)
       score2 += 1
       
        #droite
    if ball_pos[0] >= (WIDTH - (PAD_WIDTH + BALL_RADIUS)) and not(paddle2_pos <= ball_pos[1] <= (paddle2_pos + PAD_HEIGHT)):
       ball_init(False)
       score1 = int(score1)
       score1 += 1
        
     #increase velocity
        # gauche    
    if ball_pos[0] <= (BALL_RADIUS + PAD_WIDTH) and paddle1_pos <= ball_pos[1] <= paddle1_pos + PAD_HEIGHT:
        ball_vel[0] = ball_vel[0] * 1.10
        ball_vel[1] = ball_vel[1] * 1.10
        #droite
    if ball_pos[0] >= (WIDTH - (PAD_WIDTH + BALL_RADIUS)) and paddle2_pos <= ball_pos[1] <= paddle2_pos + PAD_HEIGHT:
        ball_vel[0] = ball_vel[0] * 1.10
        ball_vel[1] = ball_vel[1] * 1.10
        
        # Update ball position
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # draw ball and scores
    c.draw_circle(ball_pos, BALL_RADIUS, 1, "White", "White")
    score1 = str(score1)
    c.draw_text(score1, (150, 50), 20, "White")
    score2 = str(score2)
    c.draw_text(score2, (450, 50), 20, "White")
    
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -10
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 10
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = -10
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 10
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
button1 = frame.add_button("Reset", new_game)

new_game()


# start frame
frame.start()