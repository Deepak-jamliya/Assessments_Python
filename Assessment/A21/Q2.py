'''2)	WAP to print Square, Cube and Square Root of all numbers from 1 to N'''

import math

n = int(input("Enter N = "))
for i in range(1,n+1):
    print("\n\nSquare of ",i," is ",i**2)
    print("Cube of ",i," is ",i**3)
    print("Square root of ",i," is ",round(math.sqrt(i),2))
