'''
    A
   AB
  A_C
 A__D
ABCDE
'''

n = int(input("Enter n = "))

for i in range(1,n+1):
    print()
    char = 65

    for s in range(n-i):
        print(" ",end = "")

    for j in range(1,i+1):
        if j == 1 or j == i or i == n:
            print(chr(char),end = "")
        else:
            print("_",end= "")
        char+=1