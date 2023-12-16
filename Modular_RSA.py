from random import randint
import math

RSA = 'R'
Modular_exponentiation = 'M'

#Accepting user input of choice.
User = input("What would you like to do? Enter 'R' for RSA or 'M' forModular exponentiation: ");

if(User == 'R'):

# prime numbers for variables p & q
   def Prime():
       r = randint(100,997)

       while True:
        if newPrime(r):
            break
            
        else:
            r = r + 1
            return r
def newPrime(r):
        i = 2
        # Using math.ciel() rounds number to the nearest integer
        # math.sqrt() returns the square root of a number
        root = math.ceil(math.sqrt(r))
        
        while i <= root:
         if r % i == 0:
             return False

        
        i += 1
        return True
    
    # computing gcd
def gcd(a,b):

        while b:
            a,b = b,a % b
        return a
    
    #computing egcd
def egcd(a,b):
        if a == 0:
            return(b,0,1)
        
        else:
            g,y,x=egcd(b%a,a)
            
        return(g,x-(b//a)*y,y)
    
def modular(a,m):
         g,x,y=egcd(a,m)
         
         if g != 1:
             return None

         else:
             return x%m

if __name__ == "__main__":
    p = Prime()

    while True:
        q = Prime()

        if q != p:

            break
                
        print("p = %d"%p)
        print("q = %d"%q)
        n=p*q
        n1=(p-1)*(q-1)
        r=randint(2,100)
        
        while True:
            if gcd(r,n1)==1:

                break

            else:
                    r += 1
                    e = r
                    print("e=%d"%e)
                    d = modular(e,n1)
                    
                    print("d=%d"%d)
                    m=input("Enter message: ")

                    # the encryption 
                    c = (m**e)%n
                    print("The encryption is =%d"%c)

                    #Decryption
                    m1 = (c**d)%n
                    +print("Te decryption is =%d"%m1)

else:
    def pwr(x, y, p) : # Modular exponetiation
        num = input("Enter variable: ");
        x = x % p
        if (x == 0):
            return 0
 
        while (y > 0) :
           if ((y & 1) == 1) :
              num = (num * x) % p
              y = y >> 1
              x = (x * x) % p
              return num
     
x = 2; y = 5; p = 13
print("The power is ", pwr(x, y, p))
    


    
