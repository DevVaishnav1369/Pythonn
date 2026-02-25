import math, random
n = int (input("Enter number :" ))
if (n == 0 or n == 1 ):
    print ("Not a prime number")
else:
    for i in range (2,n+1):
        if (n % i == 0):
            print ( i )
            break
    else: print ("Prime number")
