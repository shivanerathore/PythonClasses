#Shivane Rathore
#Recursive method for string then printing reverse

#revString function
def revString(s):
    if len(s) == 0:
        return s #printing nothing if they dont enter anything
    else:
        return revString(s[1:]) + s[0] #reversing if len > 0

#getting user input and printing
string = str(input("Enter the string to be reversed: "))
print("Your reversed string is --> " + revString(string))
