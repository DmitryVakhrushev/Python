#######################################################
# Bucky_34_Subclasses Superclasses
#######################################################

# A parent "Superclass"
class parentClass:
    var1 = 'I am var1'
    var2 = 'I am var2'


# A child  class "Subclass"
# it will have all characteristics of the parent class

class childClass(parentClass):
    pass

parentObject = parentClass()
parentObject.var1

childObject.var1
childObject.var2
