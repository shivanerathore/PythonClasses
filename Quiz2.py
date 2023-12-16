# Shivane Rathore
# Write a program that reads the contents of this text file: text1.txtPreview
# the document
# The program should create a dictionary in which the keys are the individual
# words found in the file and the values are the number of times each word appears.
# For example, if the word "the" appears 20 times, the dictionary would contain
# the element with 'the' as the key and 20 as the value. 
# The program should display all of the words and their frequencies as dictionary
# items.
# Convert words to lowercase letters.
# You do NOT have to remove punctuation from the words, but if time permits,
# try removing the punctuation.

file = open("text1.txt")

dictornary = {}

while 1:
    line = file.readline()
    kt = line.split(' ');
    if not line:
        break
    for i in kt:
      try:
        dictornary[i] = dictornary[i] + 1
      except KeyError:
        dictornary[i] = 1

for key in dictornary.keys():
   print (key, dictornary[key])
