# program template for Spaceship
import simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
SHIP_ROT_INCREMENT = 0.5
SHIP_ANGLE_VEL = 0.01
ROCK_ANGLE_VEL = 0.1
SHIP_ANGLE_VEL = 0.1
CTE_FRICCION = 0.025
CTE_ACE = 0.5
MISSILE_THRUST = 4
score = 0
lives = 3
time = 0.5
current_key = ' '


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
ship_infoT = ImageInfo([135, 45], [90, 90], 35)
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


# Ship class
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
        canvas.draw_image(self.image,self.image_center, self.image_size, self.pos, self.image_size, self.angle) 

    def update(self):
        #rotar
        self.angle += self.angle_vel
        #acelerar considerando la fricción
        if self.thrust:
            forward = angle_to_vector(self.angle)
            self.vel[0] += CTE_ACE * forward[0]
            self.vel[1] += CTE_ACE * forward[1]
        self.vel[0] *= (1-CTE_FRICCION) 
        self.vel[1] *= (1-CTE_FRICCION)     
        #posicion
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.pos[0] = (self.pos[0] +  WIDTH)%  WIDTH
        self.pos[1] = (self.pos[1] +  HEIGHT)%  HEIGHT
        #sonido, imagen
        if self.thrust:
            ship_thrust_sound.play()
        else:
            ship_thrust_sound.pause()
    
    def set_angle(self, angle):
        self.angle = angle
        
    def get_angle(self):
        return self.angle
    
    def set_angle_vel(self, angle_vel):
        self.angle_vel = angle_vel
        
    def get_angle_vel(self):
        return self.angle_vel
    
    def set_thrust(self, thrust):
        self.thrust = thrust
        
    def get_thrust(self):
        return self.thrust
    
    def set_image_info(self, info):
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
  
    def shoot(self):
        global a_missile
        #missile: pos, vel, angle, angle_vel
        # posicion del cañon de la nave, velocidad la de la nave + porcentaje de impulso
        forward = angle_to_vector(self.angle)
        missile_pos = [self.pos[0] + forward[0]*self.radius, self.pos[1] + forward[1]*self.radius]
        missile_vel = [self.vel[0] + forward[0]*MISSILE_THRUST, self.vel[1] + forward[1]*MISSILE_THRUST]
        a_missile = Sprite( missile_pos, missile_vel, 0, 0, missile_image, missile_info, missile_sound)
        #print self.pos,forward, missile_pos
        #print self.vel, missile_vel
        
        
# Sprite class
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
        canvas.draw_image(self.image,self.image_center, self.image_size, self.pos, self.image_size, self.angle) 
        
        
    def update(self):
        #rotar
        self.angle += self.angle_vel
        #posicion
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
        self.pos[0] = (self.pos[0] +  WIDTH)%  WIDTH
        self.pos[1] = (self.pos[1] +  HEIGHT)%  HEIGHT
      

           
def draw(canvas):
    global time
    
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

    canvas.draw_text("Lives", (50, 50), 40, "White", "sans-serif")
    canvas.draw_text(str(lives), (50, 100), 40, "White", "sans-serif")
    canvas.draw_text("Score", (650, 50), 40, "White", "sans-serif")
    canvas.draw_text(str(score), (650, 100), 40, "White", "sans-serif")
    
    # draw ship and sprites
    my_ship.draw(canvas)
    a_rock.draw(canvas)
    if a_missile:
        a_missile.draw(canvas)
    
    
    # update ship and sprites
    my_ship.update()
    a_rock.update()
    if a_missile:
        a_missile.update()
            
# timer handler that spawns a rock    
def rock_spawner():
    global a_rock
    #random position, velocity, and angular velocity 
    #rock: pos, vel, angle, angle_vel
    rock_random_pos = [random.randrange(0, WIDTH), random.randrange(0, HEIGHT)]
    rock_random_vel = [random.random()*random.choice([-2,-1,1,2]), random.random()*random.choice([-2,-1,1,2])]
    rock_random_angle_vel = ROCK_ANGLE_VEL*random.choice([-1, -0.5,0.5, 1])
    a_rock = Sprite(rock_random_pos, rock_random_vel, 0, rock_random_angle_vel , asteroid_image, asteroid_info)

def keydown(key):
    global current_key
    current_key = chr(key)
    if key == simplegui.KEY_MAP["up"]: #impulso (acelera en la dirección de avance)
        my_ship.set_thrust(True)
        my_ship.set_image_info(ship_infoT)
    elif key == simplegui.KEY_MAP["right"]: #rotacion dcha
        #my_ship.set_angle(my_ship.get_angle()+ SHIP_ROT_INCREMENT)
        my_ship.set_angle_vel(+ SHIP_ANGLE_VEL)
    elif key == simplegui.KEY_MAP["left"]: #rotacion izd
        #my_ship.set_angle(my_ship.get_angle()- SHIP_ROT_INCREMENT)
        my_ship.set_angle_vel(- SHIP_ANGLE_VEL)
    elif key == simplegui.KEY_MAP["space"]: #disparo
        my_ship.shoot()
   
    
def keyup(key):
    global current_key
    current_key = chr(key)
    if key == simplegui.KEY_MAP["up"]: #impulso (acelera en la dirección de avance)
        my_ship.set_thrust(False)
        my_ship.set_image_info(ship_info)
    elif key == simplegui.KEY_MAP["right"]: #rotacion dcha
        my_ship.set_angle_vel(0)
    elif key == simplegui.KEY_MAP["left"]: #rotacion izd
        my_ship.set_angle_vel(0)
    elif key == simplegui.KEY_MAP["space"]: #disparo
        pass

# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship and two sprites
#ship: pos, vel, angle
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)
#rock: pos, vel, angle, angle_vel
a_rock = Sprite([WIDTH / 3, HEIGHT / 3], [1, 1], 0, ROCK_ANGLE_VEL, asteroid_image, asteroid_info)
a_missile = None
#a_missile = Sprite([2 * WIDTH / 3, 2 * HEIGHT / 3], [-1,1], 0, 0, missile_image, missile_info, missile_sound)

# register handlers
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_draw_handler(draw)

timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
timer.start()
frame.start()
