'''
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1

'''

n = int(input("Enter n = "))

for i in range(n):
    for s in range(n - i - 1):
        print(" ", end="")

    num = 1
    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)

    print()