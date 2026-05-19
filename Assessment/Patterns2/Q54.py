'''
ABCDE
 A__D
  A_C
   AB
    A
'''

n = int(input("Enter n = "))

for i in range(n, 0, -1):


    for s in range(n - i):
        print(" ", end="")

    for j in range(1, i + 1):
        if i == n:
            
            print(chr(64 + j), end="")
        elif j == 1:
        
            print("A", end="")
        elif j == i:
    
            print(chr(64 + i), end="")
        else:
            print("_", end="")
    print()