'''
    *
   **
'''

n = int(input("Enter n = "))

for i in range(1,n+1):
    print()
    j = 1
    while j <= i:
        print("*",end = "")
        j+=1

for i in range(1,n):
    print()
    k = n - i
    while k >= 1:
        print("*",end = "")
        k-=1
