'''
A B C D E
 A B C D
  A B C
   A B
    A

'''

n = int(input("Enter n: "))

for i in range(n, 0, -1):
    print(" " * (n - i), end="")
    
    for j in range(i):
        print(chr(65 + j), end=" ")
    
    print()