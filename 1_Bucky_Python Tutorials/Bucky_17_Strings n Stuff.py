#######################################################
# Bucky_17 - Strings n Stuff
#######################################################

s = 'Hey there Bucky, how is your head?'
print(s)

# we can dynamically substistue strings
# %s -- means we want to use a string variable
# e.g. varb = ('Betty','foot') describes what we want to have in both places

bucky = 'Hey there %s, how is your %s?'
varb = ('Betty','foot')
print(bucky % varb)

varc = ('Yodi','day')
print(bucky % varc)

#------------------------------------
# To find smth in the string (e.g. a word)
# "Find" method
example = 'Hey now Bessie, nice chops!'
print(example)

print(example.find('Bessie'))
print(example.find('chops'))

