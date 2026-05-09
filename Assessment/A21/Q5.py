'''
A
AB
ABC
ABCD
ABCDE'''

n = int(input("Enter N = "))

for i in range(1,n+1):
    print()
    j = 1
    ch = 65
    while j <= i:
        print(chr(ch),end = "")
        ch+=1
        j+=1
    i+=1