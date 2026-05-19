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
    j = 1
    while j<=i:
        print(chr(char),end = "")
        char+=1
        j+=1