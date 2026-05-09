'''
6. Automorphic Number Checker

A digital security company designs smart lockers that open only for
special self-matching numeric codes. When a user enters a number, the system
squares the number and checks whether the result ends with the same digits as
the original code. If yes, the locker grants access.

An automorphic number is a number whose square ends with the same number.

Example:
25² = 625

Write a program using loops to check whether the entered number is an Automorphic number.

Input:
25

Output:
Automorphic Number'''

num = int(input("Enter number : "))
sq = num**2
digit1 = 0
digit2 = 0

while num > 0:
    digit1 = num % 10
while sq > 0:
    digit2 = sq % 10

if digit1 == digit2:
    print("Automorphic Number")
else:
    print("Not an Automorphic number")

