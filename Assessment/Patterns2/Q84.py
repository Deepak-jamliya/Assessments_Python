'''
*        *
**      **
***    ***
****  ****
**********

'''

n = int(input("Enter n: "))

for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    for s in range(2 * (n - i)):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()