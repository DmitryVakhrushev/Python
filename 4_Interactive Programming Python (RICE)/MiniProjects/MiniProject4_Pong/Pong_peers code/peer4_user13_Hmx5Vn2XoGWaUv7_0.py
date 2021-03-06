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
right = True
paddle1_pos = 40.0
paddle2_pos = 40.0
paddle1_vel = 0.0
paddle2_vel = 0.0
score1 = 0
score2 = 0

# helper function that spawns a ball by updating the 
# ball's position vector and velocity vector
# if right is True, the ball's velocity is upper right, else upper left
def ball_init(right):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel = [0, 0]
    if right == True:
        ball_vel[0] = random.randrange(3, 4)
        ball_vel[1] = random.randrange(-3, -1)
    elif right == False:
        ball_vel[0] = random.randrange(-4, -2)
        ball_vel[1] = random.randrange(-3, -1)

# define event handlers

def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats
    global score1, score2 # these are ints
    paddle1_pos = 40.0
    paddle2_pos = 40.0
    paddle1_vel = 0.0
    paddle2_vel = 0.0
    score1 = 0
    score2 = 0
    ball_init(right)
    
def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, right
 
    # update paddle's vertical position, keep paddle on the screen
    if (paddle1_pos - 40) + paddle1_vel < 0 or (paddle1_pos + 40) + paddle1_vel > HEIGHT:
        pass
    else:
        paddle1_pos += paddle1_vel
    if (paddle2_pos - 40) + paddle2_vel < 0 or (paddle2_pos + 40) + paddle2_vel > HEIGHT:
        pass
    else:
        paddle2_pos += paddle2_vel
    
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # draw paddles
    c.draw_line([HALF_PAD_WIDTH, paddle1_pos - 40],[HALF_PAD_WIDTH, paddle1_pos + 40], PAD_WIDTH, "White")
    c.draw_line([WIDTH - HALF_PAD_WIDTH, paddle2_pos - 40],[WIDTH - HALF_PAD_WIDTH, paddle2_pos + 40], PAD_WIDTH, "White")
    
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # horizontal walls
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    if ball_pos[1] >= (HEIGHT - 1) - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    
    # vertical gutters and paddle collision
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        if paddle1_pos - 40 <= ball_pos[1] and paddle1_pos + 40 >= ball_pos[1]:
            ball_vel[0] = - 1.1*ball_vel[0]
        else:
            right = True
            ball_init(right)
            score2 += 1
            
    if ball_pos[0] >= ((WIDTH - 1) - BALL_RADIUS) - PAD_WIDTH:
        if paddle2_pos - 40 <= ball_pos[1] and paddle2_pos + 40 >= ball_pos[1]:
            ball_vel[0] = - 1.1*ball_vel[0]
        else:
            right = False
            ball_init(right)
            score1 += 1
        
    # draw ball and scores
    c.draw_circle(ball_pos, BALL_RADIUS, 1, 'White', 'White')
    c.draw_text(str(score1), (260, 20), 24, 'White')
    c.draw_text(str(score2), (330, 20), 24, 'White')
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= 6
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel += 6
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel -= 6
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel += 6
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
button = frame.add_button('Reset', new_game, 100)

# start frame
frame.start()

new_game()