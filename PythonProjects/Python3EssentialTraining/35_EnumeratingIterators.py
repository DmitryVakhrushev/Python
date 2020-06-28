
#==============================================================================
# Lesson #35: Enumerating iterators
#==============================================================================

def main():

    fh = open('lines.txt')
    for index, line in enumerate(fh.readlines()):
        print(index, line, end='')

    print("----------------------------------------")

    # "enumerates()" -- returns a tuple (<index>,<object>)
    a = 'Hello Kitty'
    for i in enumerate(a):
        print(i)

    print("----------------------------------------")

    s = 'This is a string'
    for i, c in enumerate(s):
        print(i,c)
        if c == 's': print('Index {} is an s'.format(i))


if __name__ == '__main__': main()

