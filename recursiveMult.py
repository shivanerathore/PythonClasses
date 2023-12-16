#Shivane Rathore
#Recursive Multiplication

def recMult(x, y):
    if x == 1:
        return y
    else:
        return y + recMult(x-1, y)

def main ():
    x = int(input("Enter an x value: "))
    y = int(input("Enter an y value: "))
    print("Your recusrive multlipication answer for " + str(x) + " x " + str(y) + " = " + str(recMult(x, y)))

if __name__ == "__main__":
    main()
