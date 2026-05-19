'''
EEEEE
DDDD
CCC
BB
A
'''

n = int(input("Enter n = "))

char = 69
for i in range(n,0,-1):
    print()
    for j in range(1,i+1):
        print(chr(char), end = "")
    char-=1
    