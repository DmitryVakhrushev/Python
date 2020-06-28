
# Restaraunt recomendation problem


'''
A sample from the big list

Georgie Porgie
87%
$$$
Canadian, Pub Food

Queen St. Cafe
82%
$
Malaysian, Thai

Dumplings R Us
71%
$
Chinese

Mexican Grill
85%
$$
Mexican

Deep Fried Everything
52%
$
Pub Food
'''

#-----------------------------------------
# dict of {str: int}
name_to_rating = {
'Georgie Porgie': 8,
'Queen St. Cafe': 82,
'Dumplings R Us': 71,
'Mexican Grill': 85,
'Deep Fried Everything': 52}

# dict {str: list of str}
price_to_names = {
'$': ['Queen St. Cafe', 'Dumplings R Us', 'Deep Fried Everything'],
'$$': ['Mexican Grill'],
'$$$': ['Georgie Porgie'],
'$$$$':[]}

# dict {str: list if str}
cuisine_to_names = {
'Canadian': ['Georgie Porgie'],
'Pub Food': ['Georgie Porgie', 'Deep Fried Everything'],
'Malaysian': ['Queen St. Cafe'],
'Thai': ['Queen St. Cafe'],
'Chinese': ['Dumplings R Us'],
'Mexican': ['Mexican Grill']}
#-----------------------------------------

# The file containing the restaraunt data
FILENAME = 'lecture_code_w1_restaurants_small.txt'

def recommend(file, price, cuisines_list):
    '''(file open for reading, str, list of syt) -> list of [int, str] list

    the output will be sorted by rating %
    '''

    # Read the file and build the data structure





    #


def read_restaraunt(file):
    '''(file) -> (dict, dict, dict)
    Return a tuple of three dictionaries based on the information in the file

    '''
    # accumulators
    














