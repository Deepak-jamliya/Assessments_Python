'''
1. Product of Odd Numbers up to N

A puzzle game rewards players by multiplying odd numbers up to n.
Write a program using loops to find product of odd numbers.

Input:
5

Output:
15
'''

num = int(input("Enter number = "))
product = 1
i = 0

while i <= num:
    if i%2 != 0:
        product = product * i
    i+=1
print(product)