# Shivane Rathore
# Write a program that writes a series of random numbers to a file.
# Each random number should be in the range of 1 through 500.
# The application should let the user specify how many random numbers the
# file will hold.

from random import randint  

def generate_number(): #function for generating rand number
   return randint(1,500)


def write_to_file(count): #function for write rand numbers to file
   with open("random numbers.txt","w") as file:
      for i in range(count):
         num = str(generate_number())
         file.write(num + "\n")
      file.close()


if __name__ == '__main__': #main
    count = int(input("Enter number of random numbers you want to generate: "))
    write_to_file(count)
