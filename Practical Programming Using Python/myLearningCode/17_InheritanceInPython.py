#===============================================================================
# 7-2: Inheritance in Python
#===============================================================================

# inheritance allows to use the same class but with some changes in it

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

#++++++++++++++++++++++++++++++++++++++++++++++
class bigCat(Cat):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
    
    def speak(self):
        return 'This a big cat'
#++++++++++++++++++++++++++++++++++++++++++++++    
        
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
    
    print(cat1, cat2)
    
    #++++++++++++++++++++++++++++++++++++++++++++++++
    cat3 = bigCat("Chebik", 12, 10) # cat3 is an object of the new class: "bigCat"
    print(cat3)
    print("My name is " + str(cat3.getName()) + ".") # getName() method is the same as it's for Cat object
    print(cat3.speak()) # Speak() method is different. It's rewritten in the new class "bigCat"
    #++++++++++++++++++++++++++++++++++++++++++++++++
    
#-------------------------------------------
if __name__ == '__main__':
    main()
    


    

 