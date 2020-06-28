def is_palindrome_v3(s):
    
    '''(str) -> bool

    Return True if and only if s is a palindrome

    >>> is_palindrome_v3('noon')
    True
    >>> is_palindrome_v3('racecar')
    True
    >>> is_palindrome_v3('dented')
    False
    '''


    i = 0 # first index of the string
    j = len(s) - 1 # last index of the string
    
    while i < j and s[i] == s[j]:
        i = i+1
        j = j-1

    return j <= i
    
