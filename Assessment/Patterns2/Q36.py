'''
ABCDE
A  D
A C
AB
A
'''

n = int(input("Enter n = "))

for i in range(n,0,-1):
    print()
    char = 65
    for j in range(1,i+1):
        if j == 1 or j == i or i == n:
            print(chr(char),end = "")
        else:
            print(" ",end = "")
        char+=1
    