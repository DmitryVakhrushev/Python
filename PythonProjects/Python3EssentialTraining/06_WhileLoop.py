
# Bill Weinman "Python 3 Essential Training"

#-------------------------------------------------------------------------------------------------
# Lesson 06 -- While Loop
#-------------------------------------------------------------------------------------------------

# sum of two elements defines the next set
# Fibonacchi series

def main():

    a, b = 0, 1
    while b < 50:
        print(b)
        a, b = b, a+b

if __name__ == '__main__': main()