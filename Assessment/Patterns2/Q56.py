'''
11111
 2222
  333
   44
    5
'''

n = int(input("Enter n = "))

for i in range(1, n + 1):
    for s in range(i - 1):
        print(" ", end="")
    
    for j in range(n - i + 1):
        print(i, end="")
    
    print()