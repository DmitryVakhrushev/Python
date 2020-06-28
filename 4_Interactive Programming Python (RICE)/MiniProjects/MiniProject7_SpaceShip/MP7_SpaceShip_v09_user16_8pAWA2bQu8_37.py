#-------------------------------
# Mini-Project Space Ship
#-------------------------------

# program template for Spaceship
import simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
score = 0
lives = 3
time = 0.5

#------------------------------
# my Variables
shootFlag = False
#------------------------------

class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

    
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)

#-------------------------------
# Ship class
#-------------------------------
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        
    def draw(self,canvas):
        #canvas.draw_circle(self.pos, self.radius, 1, "White", "White")
        #canvas.draw_image(ship_image, ship_info.center,ship_info.size,my_ship.pos,ship_info.size, my_ship.angle)

        canvas.draw_image(self.image
                          ,ship_info.center
                          ,ship_info.size
                          ,self.pos # point on the screen
                          ,ship_info.size # size on the screen
                          ,self.angle) # Rotation in radians
        
    def update(self):        
        
        #--->>> Rotation update
        self.angle += self.angle_vel
        
        #--->>> Position update
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT
        
        #--->>> Friction update
        c = 0.02
        self.vel[0] *= (1-c)
        self.vel[1] *= (1-c)
        
        #print "self.vel[0] = ", self.vel[0]
        #print "self.vel[1] = ", self.vel[1]
        
        #--->>> Thrust update
        forward = angle_to_vector(self.angle)
        #forward = [math.cos(self.angle), math.sin(self.angle)]
        
        if self.thrust == True:
            ship_info.center[0] = 135
                       
            const = 0.3
            self.vel[0] += forward[0] * const
            self.vel[1] += forward[1] * const
            
        else:
            ship_info.center[0] = 45
     
          
    def shoot(self):
        global a_missile
        global shootFlag
        
        shootFlag = True
        
        vec = angle_to_vector(self.angle)
        pos_x = self.pos[0] + vec[0] * self.radius
        pos_y = self.pos[1] + vec[1] * self.radius
        vel_x = 10 * vec[0] + self.vel[0]
        vel_y = 10 * vec[1] + self.vel[1]
        a_missile = Sprite([pos_x, pos_y], [vel_x, vel_y], self.angle, 0, missile_image, missile_info, missile_sound)

        
        #print "A missile is released"

        
#-------------------------------  
# Sprite class
#-------------------------------
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
   
    def draw(self, canvas):
        #canvas.draw_circle(self.pos, self.radius, 1, "Red", "Red")
        canvas.draw_image(self.image
                              ,asteroid_info.center
                              ,asteroid_info.size
                              ,self.pos # point on the screen
                              ,asteroid_info.size # size on the screen
                              ,self.angle) # Rotation in radians
    
    
        canvas.draw_image(self.image
                              ,missile_info.center
                              ,missile_info.size
                              ,self.pos # point on the screen
                              ,missile_info.size # size on the screen
                              ,self.angle) # Rotation in radians    	
    
    # Sprite object movement
    def update(self):
        
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        
        self.angle += self.angle_vel
        

#-------------------------------      
# Draw on Canvas    
#-------------------------------            
def draw(canvas):
    
    global time
    global shootFlag
    
    #print "shootFlag = ", shootFlag
    
    # animiate background
    time += 1
    center = debris_info.get_center()
    size = debris_info.get_size()
    wtime = (time / 8) % center[0]
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, [center[0] - wtime, center[1]], [size[0] - 2 * wtime, size[1]], 
                                [WIDTH / 2 + 1.25 * wtime, HEIGHT / 2], [WIDTH - 2.5 * wtime, HEIGHT])
    canvas.draw_image(debris_image, [size[0] - wtime, center[1]], [2 * wtime, size[1]], 
                                [1.25 * wtime, HEIGHT / 2], [2.5 * wtime, HEIGHT])

    #--->>>
    # draw ship and sprites
    my_ship.draw(canvas)
    a_rock.draw(canvas)
    
    if shootFlag == True:
        a_missile.draw(canvas)
    
    #--->>>
    # update ship and sprites
    my_ship.update()
    a_rock.update()
        
    if shootFlag == True:
        a_missile.update()
        
    #--->>>
    # draw text messages: lives and score
    canvas.draw_text("Lives", (20, 35), 25, "White", "serif")
    canvas.draw_text(str(lives), (20, 60), 25, "White", "serif")
    
    canvas.draw_text("Score", (WIDTH-100, 35), 25, "White", "serif")
    canvas.draw_text(str(score), (WIDTH-100, 60), 25, "White", "serif")
    
    
    
#----------------------------------            
# timer handler that spawns a rock    
def rock_spawner():
    global a_rock
    rockPos = [random.randint(0, WIDTH), random.randint(0, HEIGHT)]
    x = random.choice([-1,1]) * random.randrange(100, 400)/200
    y = random.choice([-1,1]) * random.randrange(100, 400)/200
    rockVel = [x,y]
    rockAngVel = random.choice([-1,1])*random.randrange(1, 200)/1000
    
    a_rock = Sprite(rockPos, rockVel, 0, rockAngVel, asteroid_image, asteroid_info)

#----------------------------------
# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

#----------------------------------
# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 4.75, ship_image, ship_info)

a_rock = Sprite([WIDTH / 3, HEIGHT / 3], [0.5, -0.5], 0, -0.07, asteroid_image, asteroid_info)

#a_missile = Sprite([2 * WIDTH / 3, 2 * HEIGHT / 3], [-1,1], 0, 0, missile_image, missile_info, missile_sound)



#------------------------------------------
# Key FUNCTIONS
#------------------------------------------
# Key RELEASED 
def keyup(key):
    
    #global shootFlag
    
    if chr(key) in "%'":
        my_ship.angle_vel = 0
        
    if chr(key) in "&": #-- Acceleration Decreases
        my_ship.thrust = False
        ship_thrust_sound.rewind()
        
    #if chr(key) in " ":
        #pass
        #shootFlag = False
        #print "space released"
        
# Key PRESSED DOWN  
def keydown(key):
    #print chr(key)
    
    if chr(key) in "%": # Left arrow -- Left Rotation
        my_ship.angle_vel = -0.11
    
    if chr(key) in "'":  # Right arrow -- Right Rotation
        my_ship.angle_vel = 0.11
        
    if chr(key) in "&": # UP arrow -- Acceleration Increases
        my_ship.thrust = True
        ship_thrust_sound.play()
        
    if chr(key) in " ":
        #print "space pressed"
        my_ship.shoot()

#----------------------------------
# register handlers
#----------------------------------
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

timer = simplegui.create_timer(1000.0, rock_spawner)

#----------------------------------
# get things rolling
#----------------------------------
timer.start()
frame.start()
