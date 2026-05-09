'''
5.

Automorphic Number Lock

A high-security digital locker validates access codes using a special mathematical rule.

When a user enters a numeric code, the system squares the number and checks whether the
last digits of the square match the original number.
If it matches, the code is considered valid.

An Automorphic Number is a number whose square ends with the same number.

Task:
Write a Python program to check whether a given number is an Automorphic Number or not.

Example:
Input:
25

Output:
Automorphic Number'''

num = int(input("Enter Number = "))
sq = num ** 2
check = 1

while num > 0:
    if num%10 != sq%10:
        check = 0
        break
    num = num // 10
    sq = sq // 10
if check:
    print("Automorphic number")
else:
    print("not Automorphic")