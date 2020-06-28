#-----------------------------------------
# Week2 -- Input/Output and str Formatting
#-----------------------------------------

print("Hello", "there!") # prints both words with a "space" in between

def square_return(num):
    return num**2

def square_print(num):
    print("The square of num is", num**2)

def sum(number1, number2):
    return number1 + number2 # return the value and stops here.
    # The "print" command will not be executed
    print("hello")

    
def sum2(number1, number2):
    print("hello")
    return number1 + number2
    
    
#---------------------------------
# Get input from a user
#---------------------------------
name = input("What is your name? ")
location = input("What is your location? ")
print(name, "lives in ", location)

#---------------------------------------
print('3,\t4,\t5') # \t --> tabulation symbols

print(name, '''\n lives in \n''', location) # \n --> print on new line
# must use ''' to use \n
print('You\'e very welcome!!!') # \ --> escape character














