'''
122Convert a binary string to decimal. 
S = "101" 
5
'''

s = input("Enter String = ")

num = int(s)
power = 0
decimal = 0

while num > 0:
    digit = num % 10
    decimal += digit * (2 ** power)
    num = num // 10
    power += 1

print(decimal)
