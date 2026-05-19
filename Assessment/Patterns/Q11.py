'''
11) Butterfly Number Pattern
    1      1
    12    21
    123  321
    12344321
    123  321
    12    21
    1      1
'''

n = int(input("Enter n = "))

for i in range(1,n+1):
    print()
    j = 1
    while j <= i:
        print(j,end = "")
        j+=1

    k = 1
    while k <= 2 * (n-i):
        print(" ",end = "")
        k+=1
    
    l = i
    while l >= 1:
        print(l,end = "")
        l-=1

for i in range(n-1,0,-1):
    print()
    j = 1
    while j <= i:
        print(j,end = "")
        j+=1
    
    k = 1
    while k <= 2 * (n-i):
        print(" ",end = "")
        k+=1

    l = i
    while l >= 1:
        print(l,end = "")
        l-=1