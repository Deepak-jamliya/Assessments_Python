'''
18) Binary Floyd Triangle
    1
    0 1
    1 0 1
    0 1 0 1
'''

n = int(input("Enter n = "))

for i in range(1,n+1):
    print()
    for j in range(1,i):
        print((i+j)%2, end = "")

