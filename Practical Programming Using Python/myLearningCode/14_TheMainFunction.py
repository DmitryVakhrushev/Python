#===============================================================================
# 5-5: The Main Function -- Kent D. Lee
#===============================================================================

# The __name__ variable is created by Python and set to the value "__main__"
# if the module being executed is the main module.
# If the module was imported into another module, then __name__ would not be set to "__main__".
# This mechanism is in place so that each module can have its own main function (for testing purposes)
# and only the main function from the main module will be executed.


def add(a,b):
    c = a+b
    return c

def mult(a,b):
    d = a*b
    return d

# Define a main() function that will run the whole code. It's not mandatory in Python as it's in other programming languages
# e.g. in Java we write Public Static Void Main function to get things started
def main():
    a = 2
    b = 7
    print(add(a,b))
    print(mult(a,b))


# It will execute the main program
if __name__ == '__main__':
    main()

# Create main() function does two things:
# 1) It hides variables that are declared in the mainfunction from the rest of the program. That makes the code more secure
# 2) If a module is imported to that program it will not have '__main__' name and won't be executed 

        