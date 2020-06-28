
# LTP2
# Week1 -- Exercise 1

def is_palindrome_v3(s):     
    """ (str) -> bool

    Return True if and only if s is a palindrome.

    >>> is_palindrome_v3('noon')
    True
    >>> is_palindrome_v3('racecar')
    True
    >>> is_palindrome_v3('dented')
    False
    """

#-----------------------------------
# Doesn't work
##    for i in range(len(s) // 2):
##        if s[i] != s[len(s) - i]:
##            return False
##
##    return True

#-----------------------------------
### Variant #2 -- Works
##    j = len(s) - 1
##    for i in range(len(s) // 2):
##        if s[i] != s[j - i]:
##            return False
##    return True

#-----------------------------------
# Works
##    for i in range(len(s) // 2 + 1):
##        if s[i] != s[len(s) - i - 1]:
##            return False
##
##    return True


#------------------------------------
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            return False

    return True



