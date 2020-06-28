#-----------------------------------------
# Coursera_29_Parallel Lists and Strings
# Parallel Lists and Strings
#-----------------------------------------

# Correspondings Elements
# Two lists are parallel if they have the same length and the items at each index are somehow related. The items at the same index are said to be at corresponding positions.

# Let's sum two lists (as vectors in R)
def sum_items(list1, list2):
    '''
    >>> list1 = [1, 2, 3]
    >>> list2 = [2, 4, 2]
    >>> sum_items([1, 2, 3], [2, 4, 2])
    '''
    sum_list = []
    for i in range(len(list1)):
        sum_list.append (list1[i] + list2[i]) # append is not equality it's a method
    return(sum_list)
    
#--------------------------------------------
# Returns the number of matches in two strings

def num_matches(s1, s2):
    ''' (str, str) -> int
    Returns the number of matches in two strings
    '''
    num_matches = 0
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            num_matches = num_matches + 1
    return num_matches

    '''
    >>> num_matches('ate', 'ape')
    >>> num_matches('head', 'hard')
    >>> num_matches('py', 'pe')

    '''
