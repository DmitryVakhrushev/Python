
# Using strings

def main():
    s = "This is a \n string!"
    print(s)

    z = r"This is a \n string with escaped new line characters" # this is called "raw string"
    print(z)

    n = 43
    # Python 3 string formatting
    k = "Use special {} string formatting".format(n)
    print(k)

    # Python 2 string formatting
    v = "Use special %s string formatting" % n
    print(v)

    # Multiline string
    m = '''\
one line
second line
third line
    '''

    print(m)
if __name__ == "__main__": main()