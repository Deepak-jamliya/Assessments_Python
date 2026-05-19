'''
123456789
 1+++++7
  1+++5
   1+3
    1

'''
n = int(input("Enter n: "))

for i in range(n, 0, -1):
    print(" " * (n - i), end="")

    for j in range(1, 2*i):
        if i == n:
            print(j, end="")
        elif j == 1 or j == 2*i - 1:
            print(j, end="")
        else:
            print("+", end="")
    print()