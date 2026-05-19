'''
7) Reverse Number Triangle
    - - - -
    2 - - -
    4 3 - -
    6 5 4 -
    8 7 6 5
'''

n = int(input("Enter n = "))

for i in range(0,n+1):
    print()
    if i == 0:
        for j in range(n):
            print("-",end = "")
    else:
        num = i * 2
        for j in range(1,n+1):
            if j<= i:
                print(num,end = "")
                num-=1
            else:
                print("-",end = "")
            