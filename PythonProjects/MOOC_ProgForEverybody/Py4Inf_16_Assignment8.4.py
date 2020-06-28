
#==========================================================
# 8.4 Open the file "romeo.txt" and read it line by line
#==========================================================
# For each line, split the line into a list of words using the split() function.
# The program should build a list of words.
# For each word on each line check to see if the word is already in the list
# and if not append it to the list. When the program completes,
# sort and print the resulting words in alphabetical order.
# You can download the sample data at http://www.pythonlearn.com/code/romeo.txt

wordList = list()
file = open('romeo.txt', mode ='r')

for line in file:
    wl = line.rstrip().split()
    for word in wl:
        if word not in wordList:
            wordList.append(word)

wordList.sort()
print(wordList)

file.close()


