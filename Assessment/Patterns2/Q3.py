'''
*
 *
  *
   *
    *
'''

n = int(input("Enter n = "))

for i in range(n+1):
    print()
    j = 1
    while j<=i:
        if j == i:
            print("*",end = "")
        else:
            print(" ",end = "")
        j+=1