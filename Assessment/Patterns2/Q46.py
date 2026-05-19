'''
    A
   AB
  ABC
 ABCD
ABCDE
'''

n = int(input("Enter n = "))


for i in range(1,n+1):
    print()
    char = 65

    for s in range(n-i):
        print(" ",end = "")

    for j in range(1,i+1):
        print(chr(char),end = "")
        char+=1
