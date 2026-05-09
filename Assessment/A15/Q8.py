'''
8.
Trimorphic Number Analyzer

A coding system checks cube-based patterns.

A Trimorphic Number:
Cube of number ends with the same number.

Example:
4³ = 64

Write a program to check Trimorphic Number.

Input:
4

Output:
Trimorphic Number'''

num = int(input("Enter Number : "))
cube = num ** 3
check = 1

while num > 0:
    if num%10 != cube%10 :
        check = 0
        break
    num = num // 10
    cube = cube // 10
if check:
    print("Trimorphic Number")
else:
    print("Not a Triomorphic Number")
