#######################################################
# Bucky_32_Object Oriented Program
#######################################################

class exampleClass:
    eyes = 'blue'
    age = 22

    def thisMethod(self):
        return 'hey this method worked'
    

exampleObject = exampleClass()

print(exampleObject.eyes)

print(exampleObject.age)

print(exampleObject.thisMethod())
