'''
x
xx
xxx
xxxx
xxx
xx
x

'''

n = int(input("Enter n: "))

for i in range(1, n + 1):
    print("x" * i)

for i in range(n - 1, 0, -1):
    print("x" * i)