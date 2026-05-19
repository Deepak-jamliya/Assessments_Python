'''
5
54
543
5432
54321
'''

n = int(input("Enter n = "))

for i in range(1, n + 1):
    print()
    num = n
    for j in range(i):
        print(num, end="")
        num -= 1