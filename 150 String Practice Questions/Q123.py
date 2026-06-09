'''
123Convert a decimal number to binary string. 
N = 5 
"101"

'''

n = int(input("Enter Number = "))
binary = ""

while n > 0:
    binary = str(n % 2) + binary
    n //= 2

print(binary)