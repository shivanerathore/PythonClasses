#Shivane Rathore
#Fibonacci Loop

import sys

def main():
    num1 = int(input("Enter your first value: "))          
    num2 = int(input("Enter your second value: ")) 
    count = 0

    while True:
        num = int(input("Enter your range: "))
        if num == 0:
            print("Cannot use this value, please choose another!")
            sys.exit() 
        elif num < 0:
            print("Please enter a positive integer: ")
        else:
            break   

    print(" ")

    while count < num:
        if count <= 1:
            nextNum = count;
        else:
            nextNum = num1 + num2;     
            print(num1, " + ", num2, " = ", nextNum)
            num1 = num2
            num2 = nextNum
        count = count + 1 

main() 
