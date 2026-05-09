'''
      *
     **
    ***   
   ****
  *****
 ******
*******
'''

n = int(input("Enter N = "))

for i in range(1,n+1):
    print()
    j = 1
    while j <= n-i:
        print(" ", end = "")
        j+=1

    k = 1
    while k<= i:
        print("*", end = "")
        k+=1
