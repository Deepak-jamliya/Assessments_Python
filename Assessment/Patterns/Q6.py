'''
6) Number Triangle with Dashes
    - - - - 1
    - - - 2 3
    - - 3 4 5
    - 4 5 6 7
    5 6 7 8 9
'''

n = int(input("Enter n ="))
for i in range(1,n+1):
    print()
    j = i
    while j <= n-1:
        print("-",end = "")
        j+=1
    
    k = i
    while k >= i and k<=i+(i-1):
        print(k,end = "")
        k+=1
