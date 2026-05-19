'''
    X 
   X X 
  X__X
 X____X
X X X X X

'''

n = int(input("Enter n = "))

for i in range(1, n + 1):

    for s in range(n - i):
        print(" ", end="")

    for j in range(1, i + 1):
        if i == n:
            print("X", end=" ")
        elif j == 1 or j == i:
            print("X", end="")
            if j != i:
                print(" ", end="")
        else:
            print("_", end="")
    print()