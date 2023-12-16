# Shivane Rathore
# Lab 2 - Sets

# Write a program that reads the contents of two text files and compares them in
# the following ways:
# -- It should display a list of all the unique words contained in both files.
# -- It should display a list of the words that appear in the first file but
#    not the second.

# creating 2 empty lists
firstFile = []
secondFile = []

# reading words from the first file (first_file.txt)
with open('first_file.txt','r') as file: 
  for line in file: 
    for word in line.split():
      firstFile.append(word)
wordSet1 = set(firstFile)

# reading words from the second file (second_file.txt)
with open('second_file.txt','r') as file: 
  for line in file: 
    for word in line.split():
      secondFile.append(word)
wordSet2 = set(secondFile)

# making a unique list
unique = firstFile + secondFile
unique = set(unique)
unique = list(unique)

print("Unique words in both files: ")
for word in unique:
  print(word) 

# printing unique words in first file
print("\nUnique words in the first file: ")
for word in wordSet1:
  print(word)

# printing unique words in second file
print("\nUnique words in the second file: ")
for word in wordSet2:
  print(word)

# printing words in both files
print("\nWords that appear in both the files: ")
wordsInBothFiles = wordSet1.intersection(wordSet2)
for word in wordsInBothFiles:
  print(word)

# finding words that appear in the first file but not the second
print("\nWords that appear in the first file but not the second file: ")
wordsInFirstFile = wordSet1.difference(wordSet2)
for word in wordsInFirstFile:
  print(word)
