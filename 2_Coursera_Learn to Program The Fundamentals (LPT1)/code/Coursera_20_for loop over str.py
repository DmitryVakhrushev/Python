#--------------------------------
# Coursera_20_for loop over str
#--------------------------------

s = 'Hi there!'
for char in s:
    print(char)


for vowel in 'aeiou':
    print("I'd like to buy a", vowel)

#--------------------------------------------------
# Write a function that calculates the number of vowels in the word
#--------------------------------------------------
def count_vowels(s):
    ''' (str) -> int

    Return the number of vowels in the string.
    Do not treat the letter y as a vowel.
    
    >>> count_vowels('Happy Anniversary!')
    5
    >>> count_vowels('xyz')
    0
    '''
    num_vowels = 0
    for char in s:
        if char in 'aeiouAEIOU':
            num_vowels = num_vowels + 1
    return num_vowels

        
#--------------------------------------------------
# Write a function that returns a string of all vowels from the string
#--------------------------------------------------

def collect_vowels(s):

    '''(str) -> str

    Return the vowels froms. Do not treat the letter y as a vowel

    >>> collect_vowels('Happy Anniversary!')
    'aAiea'
    >>> collect_vowels('xzy')
    ''
    '''
    vowels = ''
    for char in s:
        if char in 'aeiouAEIOU':
            vowels = vowels + char
    return vowels

    










