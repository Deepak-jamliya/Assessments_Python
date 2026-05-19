'''
   *
  *_* 
 *___* 
*_____*
 *___* 
  *_*
   *

'''

n = int(input("Enter n: "))

for i in range(1, n + 1):
    for s in range(n - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        if j == 0 or j == 2 * i - 2:
            print("*", end="")
        else:
            print("_", end="")
    print()

for i in range(n - 1, 0, -1):
    for s in range(n - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        if j == 0 or j == 2 * i - 2:
            print("*", end="")
        else:
            print("_", end="")
    print()