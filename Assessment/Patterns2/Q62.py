'''
    1
   123
  12345
 1234567
123456789

'''

n = int(input("Enter n = "))

for i in range(1, n + 1):
    for s in range(n - i):
        print(" ", end="")


    for j in range(1, 2 * i):
        print(j, end="")

    print()