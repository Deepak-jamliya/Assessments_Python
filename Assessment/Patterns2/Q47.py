'''
    1
   11
  1*1
 1**1
11111
'''

n = int(input("Enter n = "))

for i in range(1,n+1):
    print()

    for s in range(n-i):
        print(" ",end = "")

    for j in range(1,i+1):
        if j == 1 or j == i or i == n:
            print("1",end = "")
        else:
            print("*",end= "")