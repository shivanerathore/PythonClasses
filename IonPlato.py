# Shivane Rathore
# Assignment 3  
import string

def readFile():
    try:
        file = open(filename)
        f = file.readlines()
        w = []
        for sentence in f:
            sentence = sentence.lower()
            s = sentence.translate(str.maketrans('', '', string.punctuation))
            words = s.split()
            for word in words:
                w.append(word)
        return w
    except:
        return None

# creating dictionary 
def createDictionary(words):
    d = dict()
    for word in words:
        d[word] = 0
    for word in words:
        d[word] += 1
    return d

#alphabetically sorting dictionary
def sortDictionaryAlphabetically(d):
    sorted_d = dict()
    for key in sorted(d.keys()):
        sorted_d[key] = d[key]
    return sorted_d

#returning the dictionary word count
def topWordsCount(d):
    word_d = dict(sorted(d.items(), key = lambda x: x[1], reverse = True))
    return word_d

#taking sorted dictionary and writes into output file
def writeDictionarytoFile(d,name):
    f = open(name,'w')
    for key,value in d.items():
        #To store in output file in specified manner
        st="{:<20s} | {:>3d}".format(key,value)
        f.write(st+"\n")
    f.close()

# searching for word and word count
def noofOccur(d,filename):
    word = input("Enter the word you would like to search in the book:")
    try:
        print("The word: " + word + " occured " + str(d[word]) + " times in the book " + filename)
    except:
        print("The word " + word + " not occured in the book " + filename)

# getting the top occuring words
def topOccur(d):
    count = 0
    print("Top 10 Occurred words and their counts:")
    for keys in d.keys():
        print(keys + " : " + str(word_d[keys]))
        count += 1
        if count == 10:
            break
        
# getting the least occuring words
def leastOccur(d):
    word_d = dict(sorted(d.items(), key = lambda x:x[1]))
    count = 0
    print("Least 10 Occurred words and their counts:")
    for key in word_d.keys():
        print(key + " : " + str(word_d[key]))
        count += 1
        if count == 10:
            break

# getting the first ten words
def firstTen(d):
    count = 0
    print("First Ten words in Alphabetical Order and their counts:")
    for keys in d.keys():
        print(keys + " : " + str(d[keys]))
        count += 1
        if count == 10:
            break

# getting the last ten words
def leastTen(d):
    count = 0
    print("Last Ten words in Alphabetical Order and their counts:")
    for keys in list(d.keys())[-10:]:
        print(keys + " : " + str(d[keys]))
        count += 1
        if count == 10:
            break
  
if __name__ == '__main__':
    print("Welcome to the program: Dictionaries for Your Books!!!")
    words = None
    while(True):
        filename = input("Please enter the filename of the book that you want to create a dictionary for: ")
        words = readFile()
        if(words!= None):
            d = createDictionary(words)
            print("A dictionary is created for the book: " + filename)
            sorted_d = sortDictionaryAlphabetically(d)
            word_d = topWordsCount(sorted_d)
            writeDictionarytoFile(sorted_d,filename)
            break
        else:
            print("THIS FILE DOES NOT EXIST! TRY AGAIN!")
    while(True):
        print("\n1. Search a word and find how many times the word occurred")
        print("2. Show top 10 occurring words")
        print("3. Show the least occurring 10 words")
        print("4. Show the alphabetically first 10 words and their counts")
        print("5. Show the alphabetically last 10 words and their counts")
        print("6. Quit the program\n")
        # printing the output based on the users input
        case = int(input("Enter which your choice [1:6]: "))
        if case == 6:
            break
        if case == 1:
            noofOccur(sorted_d, filename)
        elif case == 2:
            topOccur(word_d)
        elif case == 3:
            leastOccur(d)
        elif case == 4:
            firstTen(sorted_d)
        elif case == 5:
            leastTen(sorted_d)
        else:
            print("Wrong Choice")
