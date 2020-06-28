#!/usr/bin/python3

# main script

# we can put the logic of the program into the "main" function
# (1) It runs of this is a MAIN module
# (2) this allow us to call the functions before they've been created in the script
# for example this will not work as the "egg" function was not defined before it's called

egg()
def egg():
    print("This is an egg function")


def main():
    print("This is the MainScript.py file.")

if __name__ == "__main__":
    main()