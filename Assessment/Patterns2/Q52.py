'''
12345
 1__4
  1_3
   12
    1
'''

n = int(input("Enter n = "))

for i in range(n, 0, -1):

    for s in range(n - i):
        print(" ", end="")

    for j in range(1, i + 1):
        if i == n:
            print(j, end="")
        elif j == 1 or j == i:
            print(j, end="")
        else:
            print("_", end="")
    print()