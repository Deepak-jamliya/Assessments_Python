'''
10) Slanted Star Block
    ****
     ****
      ****
       ****
'''

n = int(input("Enter n = "))

for i in range(1,n+1):
    print()
    s = 1
    while s <= i - 1:
        print(" ",end = "")
        s+=1
    
    j = 1
    while j <= n:
        print("*",end = "")
        j+=1