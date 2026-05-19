'''
   *
  *_*
 *_*_*
*_*_*_*
 *_*_*
  *_*
   *  

'''

n = int(input("Enter n: "))

for i in range(1, n + 1):
    for s in range(n - i):
        print(" ", end="")
    for j in range(1, 2 * i):
        if j % 2 == 0:
            print("_", end="")
        else:
            print("*", end="")
    print()

for i in range(n - 1, 0, -1):
    for s in range(n - i):
        print(" ", end="")
    for j in range(1, 2 * i):
        if j % 2 == 0:
            print("_", end="")
        else:
            print("*", end="")
    print()