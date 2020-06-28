#######################################################
# Bucky_35_Overwrite Variable on Sub
#######################################################

class parent:
    var1 = 'bacon'
    var2 = 'sausage'


class child(parent):
    var2 = 'toast'

pob = parent()
cob = child()

pob.var1
pob.var2

cob.var1
cob.var2



