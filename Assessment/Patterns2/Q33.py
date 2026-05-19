'''
ABCDE
ABCD
ABC
AB
A
'''

n = int(input("Enter n = "))

for i in range(n,0,-1):
    print()
    char = 65
    for j in range(1,i+1):
        print(chr(char),end = "")
        char+=1