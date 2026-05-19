'''
    5
   44
  333
 2222
11111
'''

n = int(input("Enter n = "))

for i in range(n, 0, -1):

    for s in range(i - 1):
        print(" ", end="")
    

    for num in range(n - i + 1):
        print(i, end="")
    
    print()