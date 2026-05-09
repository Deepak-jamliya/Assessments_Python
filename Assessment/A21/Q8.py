''' 
654321
 65432
  6543
   654
    65'''

n = int(input("Enter N = "))

for i in range(1,n):
    print()

    s = 1
    while s <= i - 1:
        print(" ",end = "")
        s+=1

    j = n
    while j >= i:
        print(j,end = "")
        j-=1