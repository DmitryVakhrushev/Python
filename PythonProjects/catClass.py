
#-------------------------------
# Class Cat with the method "Meo"
#-------------------------------

class Cat:
    def __init__(self, name, age, weight):
        self._name = name
        self._age = age
        self._weight = weight


    def speak(self):
        if (self._weight > 2):
            return "meow"


#-------------------------------
# A fucntion
#-------------------------------
def hello(z):
    '''requires a string'''
    print("Hello Kitty",z)


hello('Dmitry')
print(help(hello)) # shows the docstring for the function "Hello"

print(dir(Cat)) # shows methods of the class Cat