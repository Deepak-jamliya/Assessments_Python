'''
1
00
111
0000
11111
'''

n = int(input("Enter n = "))

for i in range(n+1):
    print()
    for j in range(i):
        if i%2 == 0:
            print("0",end = "")
        else:
            print("1",end = "")
        
