'''
1) Hollow Pyramid
        *
       * *
      *   *
     *     *
    *********
'''


n = int(input("Enter n = "))

for i in range(1, n + 1):
    print()
    for j in range(1, 2*n):
        if j == n - i + 1 or j == n + i - 1 or i == n:
            print("*", end="")
        else:
            print(" ", end="")