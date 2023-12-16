# Shivane Rathore
# Assignment 2 - Encoding English Civil War Ciphers

# using to detect punctuations
import string

# reading the file and reutrning the content of file
def load_text(trevanion):
    file = open('trevanion.txt', "r")
    return file.read()
   
# printing the message and code for all offsets 
def solve_null_cipher(message,numberOfLetters):
    message = "".join(message.split())
    for i in range(1, numberOfLetters + 1):
        print("Using offset of", i, "after punctuation = ", end = "")
        for j in range(0, len(message) - i):
            if(message[j] in string.punctuation):
                isPuncAfter = False
                for k in range(1, i + 1):
                    if message[j + k] in string.punctuation:
                        isPuncAfter = True
                        break
                if(isPuncAfter):
                    continue
                print(message[j + i], end = "")
        print()

# main to start execution
def main():
    trevanion = input("Enter full filename for message to translate: ")
    message = load_text(trevanion)
    print("ORIGINAL MESSAGE = ")
    print(message)
    print(" ")
    print("List of punctuation marks to check = ", string.punctuation)
    print(" ")
    numberOfLetters = int(input("Number of letters to check after punctiation mark :"))
    print(" ")
    solve_null_cipher(message, numberOfLetters)
    

# calling main
main()
