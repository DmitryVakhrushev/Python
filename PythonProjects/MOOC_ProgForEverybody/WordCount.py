

# Program to find the most common word in a text file

fileName = 'textForWordCount.txt'

handle = open(fileName, 'r')
text = handle.read()
words = text.split()
counts = dict()

for word in words:
    counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print (bigword, bigcount)