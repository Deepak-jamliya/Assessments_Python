'''
30) Extended Slanted Star Block
    ****
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

    for j in range(1,n):
        print("*",end = "")
        