'''
3. Composite Number Detector

A product testing company labels batch numbers as risky if they have more than two factors.
Such numbers are known as composite numbers and indicate repeated grouping patterns.

The quality control officer enters a batch number, and the software checks whether it is
Composite or Not.

Write a program to check whether a number is Composite or Not.

Input:
12

Output:
Composite Number
'''

num = int(input("Enter Number = "))

is_prime = 0
i = 2

while i <= num//2:
    if num%i == 0:
        is_prime = 1
        break
    i+=1
if is_prime:
    print("Composite Number")
else:
    print("Prime Number")