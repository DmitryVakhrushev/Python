#===============================================================================
# 3.4 - The Accumulator Pattern for Lists -- Kent D. Lee 
#===============================================================================

#Checking sentence --> 'How are you doing? Today is a fine day for a bycicle ride.'

s = input("Please enter a sentence: ")
lst = s.split()

# Initialize our accumulators
count = 0 
wordLenghts = 0

for word in lst:
    count +=1
    wordLenghts += len(word)
    
avgWordLength = wordLenghts / count

print('The sentence you enter has'
      , count
      , 'words in it and the average word length is %1.2f.' % avgWordLength)

