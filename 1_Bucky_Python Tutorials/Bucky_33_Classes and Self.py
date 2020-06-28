#######################################################
# Bucky_33_Classes and Self
#######################################################

# We can create functions inside of the class
# Those functions are METHODS
# Every parameter in the class should take 'self' and # any other parameters

#-----------------------------
# Defining a class

class className:

# Let's create 3 methods inside of the class

    def createName(self, name):
        self.name = name

    def displayName(self):
        print(self.name)
        #return self.name

    def saying(self):
        print('hello %s' % self.name)

# Creating objects that belong to the created class
# Any time you created an object
# you can use any of the methods inside of this object

#-----------------------------
# Let's create two objects
first = className()
second = className()

#-----------------------------
# Use the methods
#-----------------------------
first.createName('bucky') # this methods requires one parameter
second.createName('tony')

first.displayName()
first.saying()
