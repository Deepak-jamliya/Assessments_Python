'''
    A
   B B
  C  C
 D    D
EEEEEEEEE

'''

n = int(input("Enter n: "))

for i in range(1, n + 1):
    print(" " * (n - i), end="")

    ch = chr(64 + i)

    if i == 1:
        print(ch)
    elif i == n:
        print(ch * (2 * n - 1))
    else:
        print(ch + " " * (2 * i - 3) + ch)