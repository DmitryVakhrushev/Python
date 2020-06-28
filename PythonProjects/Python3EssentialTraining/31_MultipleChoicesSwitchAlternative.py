
#----------------------------------------------------------------------
# Lesson #31: Understanding other strategies for multiple choices
#----------------------------------------------------------------------

# Alternative to SWITCH function that exists in other languages
# We can use dictionary to tackle this problem


def main():

    choices = dict( one = 'First'
                   ,two ='Second'
                   ,three ='Third')

    v = 'one'
    # print(choices[v]) -- this throws an error if the key doesn't exist
    print(choices.get(v,'Other'))

    v = 'five'
    print(choices.get(v,'Other')) # Returns other if the key doesn't exist

if __name__ == '__main__': main()



