
def main():

    #----------------------------
    # Tuples
    x = (1, 2, 3, 4, 5) # Tuple is immutable objects
    print(type(x), x)

    for i in x:
        print(i)

    #----------------------------
    # lists are mutable
    y = [1, 2, 3]
    print(type(y), y)
    y.append(5)
    y.insert(2,7)
    print(type(y), y)

    #----------------------------
    #string
    z = 'string'
    print(type(z), z[2:4])
    for i in z:
        print(i)


if __name__ == "__main__": main()
