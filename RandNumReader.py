# Shivane Rathore
# By using the .txt file that you created in the Problem 1, write another program
# that reads the random numbers from the file and displays the following information
# - The total of the numbers
# - The max of the numbers
# - The min of the numbers

# function to read random numbers from file to a list and returns
# the list
def readRandomNumbers():
   numbers = list()
   with open("random numbers.txt","r") as file:
      for line in file:
         numbers.append(int(line.rstrip()))
      file.close()
   return numbers

# max and min
def MaxAndMin():
   with open("random numbers.txt", "r") as file:
      for line in file:
         max(numbers)
         min(numbers)
      file.close()
   return numbers

# printing
def displayData(numbers):
   print("The total of the numbers: %d" %sum(numbers))
   print("The number of random numbers read from the file : %d" %len(numbers))
   print("The max and min of the numbers from the file: %d" %max(numbers), min(numbers))

# main function
if __name__ == '__main__':
    randomNumbers = readRandomNumbers()
    displayData(randomNumbers)
