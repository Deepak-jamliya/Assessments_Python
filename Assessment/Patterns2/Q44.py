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

    for space in range(n-i):
        print(" ",end = "")
    
    for j in range(1,i+1):
        print(i,end = "")
