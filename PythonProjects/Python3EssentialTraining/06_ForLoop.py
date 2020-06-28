
# For Loop

# Read the lines from the file
# "Iterator" is the object which gives you the new value each time it's called


#-------------------------------------------
# "fh.readlines()" is an iterator
#-------------------------------------------
def main():

    fh = open('lines.txt')
    for line in fh.readlines():
        print(line, end='')

if __name__ == '__main__': main()