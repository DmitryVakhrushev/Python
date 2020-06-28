
# Lesson 19 -- Creating and using functions

def main():
    func()
    func(2)
    func(3)


def func(a = 7): # with the default value of "7"
    for i in range(a, 10):
        print(i, end=' ')
    print()


if __name__ == "__main__": main()


