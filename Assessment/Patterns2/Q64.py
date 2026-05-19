'''
    *
   *_*
  *___* 
 *_____* 
*********

'''

n = int(input("Enter n = "))

for i in range(1, n + 1):

    for s in range(n - i):
        print(" ", end="")

    for j in range(1, 2 * i):
        if i == 1:
            print("*", end="")
        elif i == n:
            print("*", end="")
        elif j == 1 or j == 2 * i - 1:
            print("*", end="")
        else:
            print("_", end="")
    print()