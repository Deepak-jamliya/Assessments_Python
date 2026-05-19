'''
A
BCD
EFGHI
JKLMNOP
'''

n = int(input("Enter n = "))

char = 65

for i in range(1,n+1):
    print()
    for j in range(2*i-1):
        print(chr(char),end = "")
        char+=1
