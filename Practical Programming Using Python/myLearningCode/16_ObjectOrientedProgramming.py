#===============================================================================
# 7-1: Object-Oriented Programming -- Kent D.Lee
#===============================================================================

# If I want to describve a "cat" object I need to write (declare) a "cat" class first
# The First part of the class is called a "Constructor" and it has a special name __init__
# In that constructor we declare attributes that we want to provide whem declare a cat object

# Inside of the class we create methods -- actions that may be used on the class's objects

#---------------------------------------------
# Defining a class and methods of the class
#---------------------------------------------
# 'self' parameter is an object itself 
# self is a special pointer to the object I am working with right now

class Cat:
    def __init__ (self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        self.stomach = 0

    def feed(self, amount):
        self.stomach = self.stomach + amount
    
    def nextDay(self):
        # it takes of 1/4 pound of cat feed per day to keep cat alive
        self.weight = self.stomach + self.weight - 0.25
        self.stomach = 0
        
    def speak(self):
        if self.stomach > 0:
            return('purrrrr')
        else:
            return('meow!!!')

    # Create a getName method. This method may be used on a "cat" object 
    def getName(self):
        return self.name

    def getWeight(self):
        return self.weight
    
#-------------------------------------------
def main():
    cat1 = Cat("Curious", 10, 7.2)
    cat2 = Cat('Mother', 15, 14.3)
    
    print(cat1.getName(),'says',cat1.speak())
    print(cat2.getName(),'says',cat2.speak())
    
    cat1.feed(2)
    cat2.feed(1)
    
    print(cat2.getName(),'says',cat2.speak())
    
    cat1.nextDay()
    cat2.nextDay()
    
    print(cat1.getName(),'weighs',cat1.getWeight())
    print(cat2.getName(),'weighs',cat2.getWeight())
    
#-------------------------------------------
if __name__ == '__main__':
    main()
    
    
    

 