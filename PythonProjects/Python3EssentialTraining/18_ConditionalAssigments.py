
# Lesson 18 -- Selecting code and values with conditionals

#--------------------------------------------
# Conditional Execution
def cond():
    c, d = 6, 12
    if c < d:
        print("Less")
    elif c > d:
        print("More")
    else:
        print("Equal")
#--------------------------------------------
# Conditional Expressions (assigments)
def main():
    a, b = 9, 7
    s = "A is bigger than B" if a > b else "A <= B"
    print(s)
#--------------------------------------------
if __name__ == "__main__":
    main()
    cond()

