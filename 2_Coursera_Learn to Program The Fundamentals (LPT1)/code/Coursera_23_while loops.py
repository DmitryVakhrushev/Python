#--------------------------------
# Coursera_21_while loops
#--------------------------------

num = 2
while num < 100:
    print(num)
    num = num *2

#---------------------------
s = 'hello'
for char in s:
    print(char)

#-------------------------------
# Print print until it comes across a vowel in the word
# Python performs "lazy evaluation" of its 'and' operation:
# if the first condition is FALSE it won't check the second one.
def show_first_cons(s):
    i = 0
    while i < len(s) and not(s[i] in 'aeiouAEIOU'):
        print(s[i])
        i = i + 1

show_first_cons('Hello')
show_first_cons('xyz')

#------------------------------------
def up_to_vowel(s):
    ''' (str) -> str

    Return a substring of s from index 0 up to but
    not including the first vowel in s.

    >>> up_to_vowel('hello')
    'h'
    >>> up_to_vowel('there')
    'th'
    >>> up_to_vowel('cs')
    'cs'
    '''

    before_vowel = ''
    i = 0

    while i < len(s) and not (s[i] in 'aeiouAEIOU'):
        before_vowel = before_vowel + s[i]
        i = i + 1

    return before_vowel











