
#==============================================================================
# Lesson #36: Controlling loop flow with break continue and else
#==============================================================================

def main():

    s = 'This is a string'


    # Using "continue" to skip an iteration
    for c in s:
        if c == 's': continue # skipping all "s" letters
        print(c, end='') # printing one letter at a time


    print("---------------------------------------------------------")
    # Using "break" to exit the loop completely
    for c in s:
        if c == 's': break
        print(c, end='')

    print("---------------------------------------------------------")
    # Using "else" to add logic
    for c in s:
        if c == 's':
            continue # skipping all "s" letters
        print(c, end='') # printing one letter at a time
    else:
        print("EXTRA")

if __name__ == '__main__': main()