
#------------------------------------------------------------
# Lesson #26: Creating associative lists with dictionaries
#------------------------------------------------------------


def main():
    d1 = {'one':1, 'two':2, 'three':4, 'four':4, 'five':5}
    print(d1)

    for key in d1:
        print(key, d1[key])


    # Sort dictionary by KEY
    print("-----------------------------------------")
    for key in sorted(d1.keys()):
        print(key, d1[key])


    print("-----------------------------------------")
    # Another way to define a dictionary
    d2 = dict(One = 1, Two = 2, Three=3, Four=4, Five='five')

    d2['Seven'] = 7 # Dictionaries are mutubale objects

    for key in sorted(d2.keys()):
        print(key, d2[key])





if __name__ == "__main__": main()