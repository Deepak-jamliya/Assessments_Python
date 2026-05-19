'''
15) Zig-Zag Star
    *   *   *
      *   *
    *   *   *
'''

n = int(input("Enter n ="))

for i in range(1,n-1):
    print()
    j = 1
    while j <= n:
        if i %2 != 0:
            if j%2 == 0:
                print(" ",end = "")
            else:
                print("*",end = "")
        else:
            if j%2 == 0:
                print("*",end = "")
            else:
                print(" ",end = "")
        j+=1
