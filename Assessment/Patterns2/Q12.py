'''
a
ab
abc
abcd
abcde
'''

n = int(input("Enter n = "))

for i in range(n):
    print()
    char = 97
    for j in range(i+1):
        print(chr(char),end = "")
        char+=1
