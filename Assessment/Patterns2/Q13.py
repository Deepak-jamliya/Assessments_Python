'''
1
01
101
0101
10101
'''

n = int(input("Enter n = "))

for i in range(n+1):
    print()
    num = 1 if i%2 != 0 else 0
    j = 1
    while j<=i:
        print(num,end = "")
        num = 1 - num
        j+=1
        