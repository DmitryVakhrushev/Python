#---------------------------------
# Quiz 3a
#---------------------------------

def date(month, day):
    """
    Given numbers month and day, returns a string of the form '2/12',
    with the month followed by the day.
    """
    return str(month) + "/" + str(day)

print date(2, 12)


x = "1lll1l1l1l1ll1l111ll1l1ll1l1ll1ll111ll1ll1ll1l1ll1ll1ll1ll1lll1l1l1l1l1l1l1l1l1l1l1l1ll1lll1l111ll1l1l1l1l1"
print len(x)

counter = 0
print x
for i in x:
    if i=='l':
        counter +=1
print counter


#float("5 five")
float("5.4")
#int("five")
float("5")  

print(x.count("l"))

word = 'Mississippi'
print (word.count("i"))

#-----------------------------------------------
import simplegui

def pic(can):
    can.draw_circle((90, 200), 20, 10, "White")
    can.draw_circle((210, 200), 20, 10, "White")
    can.draw_line((50, 180), (250, 180), 40, "Red")
    
    can.draw_line((55, 170), (90, 120), 5, "Red")
    can.draw_line((90, 120), (130, 120), 5, "Red")
    
    can.draw_line((180, 108), (180, 160), 140, "Red")


f = simplegui.create_frame("Object", 300, 300)
f.set_draw_handler(pic)

f.start()
#-----------------------------------------------