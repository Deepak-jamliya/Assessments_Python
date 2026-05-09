'''
9.
Abundant Number Detector

A financial system analyzes surplus numbers.

An Abundant Number:
Sum of proper factors > number

Write a program to check Abundant Number.

Input:
12

Output:
Abundant Number'''

num = int(input("Enter Number = "))

sum = 0
i = 1
while i < num:
    if num%i == 0:
        sum = sum + i
    i+=1

if sum > num:
    print("Abundant Number")
else:
    print("Not Abundant")