
#---------------------------------------------------
# Import a Class that I wrote
# import sys
# print(sys.path)

#sys.path.append('c:/111/myFirstPyProject/')
#sys.path.insert('/111/myFirstPyProject/')
#print(sys.path)

import catClass


a = 10
b = 20

print(a+b)

def abc(z):
    return z + 150

print(abc(20))

catClass.hello()

cat1 = catClass.Cat("Chebika",10,12)
#
print(cat1._weight)
print(cat1.speak())