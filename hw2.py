#Shivane Rathore
#Assignment 2: Preprocessing by using NLTK Start Assignment

#importing packages
from nltk import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

#Returns the file content.
def readFile(filename):
    file = open(filename)
    text = file.read()
    file.close()
    return text

#Printing the contents of the file
print("File contents:")
file = readFile('starshipSN8News.txt')
print(file)

#It returns the tokenized words. It will be better to remove the stop words 
#and special characters in here and return the tokenized word afterwords.
def get_tokens(text):
    stopWords = set(stopwords.words('english'))
    tokenizer = RegexpTokenizer(r"\w+")
    tokens = tokenizer.tokenize(text)
    filterTokens = []
    for w in tokens:
        if w not in stopWords:
            filterTokens.append(w)
    return filterTokens

#Printing the tokenized words
print(" ")
print("Tokenization:")
tokens = get_tokens(file)
print(tokens)

#It will accept the tokens generated in the get_tokens function and create a dictionary with 
#the root word as a key and its' count as value. Returns the dictionary. Lemmatization must be done in this 
def createDictionary(wordList):
    lemmatizer = WordNetLemmatizer()
    dict1 = {}
    for word in wordList:
        word = lemmatizer.lemmatize(word)
        if word not in dict1.keys():
            dict1[word] = 1
        else:
            dict1[word] += 1
    return dict1

#Printing dictionary
print(" ")
print("Dictionary:")
dictionary = createDictionary(tokens)
print(dictionary)

#Takes dictionary as an argument and returns the sorted dictionary according to word counts (values).
def topWordCounts(dictionary):
    return dict(sorted(dictionary.items(), key = lambda item: item[1],reverse = True))

#Printing word counts
print(" ")
print("Word Counts:")
topDict = topWordCounts(dictionary)
print(topDict)

#Printing top word counts
print(" ")
print("Top Word Counts:")
topDictWords = list(topDict.keys())
for i in range(10):
    print(f'{topDictWords[i]}: {topDict[topDictWords[i]]}')