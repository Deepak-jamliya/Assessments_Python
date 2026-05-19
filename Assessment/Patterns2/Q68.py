'''
    #
   *#* 
  **#** 
 ***#*** 
****#****

'''

n = int(input("Enter n: "))

for i in range(n):
    print(" " * (n - i - 1), end="")

    print("*" * i, end="")

    print("#", end="")

    print("*" * i)