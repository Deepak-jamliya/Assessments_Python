'''
54321
5432
543
54
5
'''

n = int(input("Enter n = "))

for i in range(n,0,-1):
    print()
    for j in range(n,n-i,-1):
        print(j,end = "")