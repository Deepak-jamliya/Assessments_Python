'''
a
bc
def
ghij
klmno
'''

n = int(input("Enter n = "))

char = 97
for i in range(1,n+1):
    print()
    for j in range(i):
        print(chr(char),end = "")
        char+=1
