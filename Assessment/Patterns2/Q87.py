'''
    1
    2
    3
    4
123454321
    4
    3
    2
    1

'''

n = int(input("Enter n: "))

for i in range(1, n):
    for s in range(n - 1):
        print(" ", end="")
    print(i)

for i in range(1, n + 1):
    print(i, end="")
for i in range(n - 1, 0, -1):
    print(i, end="")
print()

for i in range(n - 1, 0, -1):
    for s in range(n - 1):
        print(" ", end="")
    print(i)