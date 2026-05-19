'''
a
bc
d f
g  j
klmno
'''

n = int(input("Enter n = "))

char = 97
for i in range(1,n+1):
    print()
    for j in range(1,i+1):
        if j == 1 or j == i or i == n:
            print(chr(char),end = "")
        else:
            print(" ",end = "")
        char+=1
