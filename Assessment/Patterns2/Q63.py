'''
    A
   ABC
  ABCDE
 ABCDEEF
ABCDEFGHI

'''

n = int(input("Enter n = "))

for i in range(1, n + 1):

    for s in range(n - i):
        print(" ", end="")


    for j in range(1, 2 * i):
        print(chr(64 + j), end="")

    print()