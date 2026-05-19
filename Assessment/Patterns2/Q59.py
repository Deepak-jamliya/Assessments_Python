'''
    A
   A B
  A B C
 A B C D
A B C D E  

'''

n = int(input("Enter n = "))

for i in range(1, n + 1):
    for s in range(n - i):
        print(" ", end="")
    
    for j in range(1, i + 1):
        print(chr(64 + j), end=" ")
    
    print()