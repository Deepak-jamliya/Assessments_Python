'''
***** *****
****   ****
***     ***
**       **
*         *
*         *
**       **
***     ***
****   ****
***** *****

'''

n = int(input("Enter n: "))

for i in range(n, 0, -1):
    for j in range(i):
        print("*", end="")
    for s in range(2 * (n - i) + 1):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()

for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    for s in range(2 * (n - i) + 1):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()