'''
1
1 2
1  3
1   4
1  3
1 2
1

'''

n = int(input("Enter n: "))

for i in range(1, n + 1):
    print(1, end="")
    for j in range(i - 1):
        print(" ", end="")
    if i > 1:
        print(i, end="")
    print()

for i in range(n - 1, 0, -1):
    print(1, end="")
    for j in range(i - 1):
        print(" ", end="")
    if i > 1:
        print(i, end="")
    print()