'''
1
22
333
4444
55555
'''

n = int(input("Enter n = "))

for i in range(1,n+1):
    print()
    j = 1
    while j<=i:
        print(i,end = "")
        j+=1