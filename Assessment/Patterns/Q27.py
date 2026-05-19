'''
27) Continuous Number Pyramid
            1
           2 3
          4 5 6
         7 8 9 10
'''

n = int(input("Enter n = "))
num = 1

for i in range(1,n+1):
    print()
    for s in range(n-i):
        print(" ",end = "")
    
    for j in range(1,i):
        if num<=10:
            print(num,end = " ")
            num+=1


