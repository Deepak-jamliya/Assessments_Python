'''
1. Prime Security Code Checker

A high-security research lab uses numeric passcodes to unlock restricted doors. To improve security,
only prime numbers are accepted because they have exactly two factors and are harder to predict 
using common patterns.

When an employee enters a code, the system must verify whether the number is prime. If yes,
access is granted; otherwise, access is denied.

Write a program to check whether the entered number is Prime or Not Prime.

Input:
29

Output:
Prime Number
'''

num = int(input("Enter Number = "))

if num <= 0:
    print("Not Prime")
else:
    is_prime = 1
    i = 2
    while i <= num//2:
        if num%i == 0:
            is_prime = 0
            break
        i+=1
        
if is_prime:
    print("Prime Number")
else:
    print("Not a Prime Number")
