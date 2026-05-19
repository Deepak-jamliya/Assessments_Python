'''
A
AB
A C
A  D
ABCDE
'''

n = int(input("Enter n = "))

for i in range(1,n+1):
    print()
    char = 65
    for j in range(1,i+1):
        if j == 1 or j == i or i == n:
            print(chr(char),end = "")
        else:
            print(" ",end = "")
        char+=1