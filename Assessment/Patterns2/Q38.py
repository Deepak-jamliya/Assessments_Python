'''
55555
4  4
3 3
22
1
'''


n = int(input("Enter n = "))

for i in range(n,0,-1):
    print()
    for j in range(1,i+1):
        if j == 1 or i == j or i == n:
            print(i,end = "")
        else:
            print(" ",end= "")