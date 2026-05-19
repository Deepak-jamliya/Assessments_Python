'''
A
BB
CCC
DDDD
EEEEE
'''

n = int(input("Enter n = "))

char = 65
for i in range(1,n+1):
    print()
    for j in range(i):
        print(chr(char),end = "")
    char+=1
