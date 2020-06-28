#######################################################
# Bucky_28_Default Parameyers
#######################################################

def name(first,last):
    print ('%s %s' % (first,last))


name('bucky', 'roberts')

#-------------------------
# With a default parameter

def name(first='Tom',last='Smith'):
    print ('%s %s' % (first,last))

name()
name('bucky', 'roberts')
name('bucky')
name(last='roberts')
