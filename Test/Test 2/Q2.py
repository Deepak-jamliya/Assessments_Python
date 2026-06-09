'''2.
A graphics rendering engine displays signal strength in a diamond-shaped visualization.

Write a Python program to print a star diamond pattern.

Input
Enter number of rows: 5

    *
   ***
  *****
 *******
********* 
 *******
  *****
   ***
    *
'''

n = int(input("Enter N = "))

for i in range(1,n+1):
    print()
    for s in range(n-i):
        print(" ",end = "")
    for j in range(2*i-1):
        print("*",end = "")


for i in range(n-1,0,-1):
    print()
    for s in range(n-i):
        print(" ",end = "")
    for j in range(2*i-1):
        print("*",end = "")

    