file = open("nText.txt",'r')
words = 0
lines = 0 

for line in file:
    lines = lines + 1
    wordList = line.split(" ")
    for word in wordList:
        words = words + 1

print('Average number of words per line ',words/lines)
