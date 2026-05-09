'''
a
ab
abc
abcd
abcde
'''

n = int(input("Enter N = "))

for i in range(1,n+1):
    print()
    j = 1
    ch = 97
    while j <= i:
        print(chr(ch),end = "")
        ch+=1
        j+=1
    i+=1