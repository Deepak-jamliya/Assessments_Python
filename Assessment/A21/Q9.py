'''
    1
   10
  101
 1010
10101      
'''

n = int(input("Enter N = "))

for i in range(1,n+1):
    print()
    s = n
    while s > i:
        print(" ",end = "")
        s-=1
    j = 1
    while j<=i:
        if j%2 == 0:
            print("0",end = "")
        else:
            print("1",end = "")
        j+=1

    