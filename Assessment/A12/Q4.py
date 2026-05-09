'''
4. Strong Number Checker

A digital lock opens only for strong numbers.

A strong number is a number whose sum of factorial of digits equals the number.

Example:
145 = 1! + 4! + 5!

Write a program using loops to check strong number.

Input:
145

Output:
Strong Number
'''

num = int(input("Enter Number = "))
sum = 0
check = num

while num > 0:
    digit = num % 10
    factor = 1
    i = 1
    while i <= digit:
        factor = factor * i
        i+=1
    sum = sum + factor
    num = num // 10

if sum == check:
    print("Strong Number")
else:
    print("Not a strong number")
    

