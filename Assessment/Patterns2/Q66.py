'''
    1 
   1*1
  1***1
 1*****1
111111111

'''

n = int(input("Enter n: "))

for i in range(1, n + 1):
    print(" " * (n - i), end="")

    if i == 1:
        print("1")
    elif i == n:
        print("1" * (2 * n - 1))
    else:
        print("1" + "*" * (2 * i - 3) + "1")