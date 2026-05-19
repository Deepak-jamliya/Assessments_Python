'''
2) Hollow Rectangle
    *********
    *       *
    *       *
    *       *
    *********

'''

n = int(input("Enter n = "))

for i in range(1,n+1):
    print()
    i = 1
    while i <= n*2-1:
        print("*",end = "")
        i+=1

    s = 2