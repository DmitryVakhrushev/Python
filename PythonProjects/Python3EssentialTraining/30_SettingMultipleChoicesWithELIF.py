
#---------------------------------------------------------
# Lesson #30: Setting multiple choices with elif
#---------------------------------------------------------

# ONLY ONE of the conditions below will be executed

def main():
    v = 'seven'
    if v == 'one':
        print('v is one')
    elif v == 'two':
        print('v is two')

    elif v == 'three':
        print('v is three')
    else:
        print('v is some other thing')

if __name__ == '__main__': main()