# format function

def format(t):
    
    minutes = str(t // 600)
    
    if ((t - (t//600)*600) // 10) < 10:
        seconds = "0" + str((t - (t//600)*600) // 10)
    else:
        seconds = str((t - (t//600)*600) // 10)
    
    #seconds = (t - (t//600)*600) // 10
    
    millis = str(t%10)
    
    print minutes + ":" + seconds  + "." + millis

format(0)
format(11)
format(60)
format(90)
format(321)
format(599)
format(602)
format(613)
format(667)
format (1328)
format(5999)

print ""
print "Minutes----------------------"
# minutes
print 11//600
print 321//600
print 613//600
print 614//600
print 1328//600


print ""
print "Seconds----------------------"
print 11//10
print 60//10
print 321//10
print "602 -->" + str(602//10)
print "667 -->" + str(667//10)

print (667 - (667//600)*600)//10
print""

print 613//10
print 614//10
print 1328//10


print ""
print "MILLIiseconds----------------------"
# milliseconds
print 11%10
print 321%10
print 613%10
print 614%10
print 1328%10


format(0)
format(7)
format(17)
format(60)
format(63)
format(214)
format(599)
format(600)
format(602)
format(667)
format(1325)
format(4567)
format(5999)

###################################################
# Output from test

#0:00.0
#0:00.7
#0:01.7
#0:06.0
#0:06.3
#0:21.4
#0:59.9
#1:00.0
#1:00.2
#1:06.7
#2:12.5
#7:36.7
#9:59.9





