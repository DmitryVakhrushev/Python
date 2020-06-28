#######################################################
# Bucky_36_Multiple Parent Classes
#######################################################

class Mom:
    var1 = 'Hey, I am mom'

class Dad:
    var2 = 'Dad is here'

class child(Mom, Dad):
    var3 = 'I am a new variable'


childObject = child()

child.var1
child.var2
child.var3



