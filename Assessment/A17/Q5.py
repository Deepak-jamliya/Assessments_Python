'''
5.
Tech Number Checker

A number is called a Tech Number if:

It has even number of digits
Split it into two equal halves
Add both halves
Square the sum
If result equals original number → Tech Number

Write a program to:

Count digits
If digits are even, split the number
Find sum of both halves
Square the sum
Display intermediate values
Check and print result

Input:
2025

Output:
First Half = 20
Second Half = 25
Sum = 45
Square = 2025
Tech Number'''

num = int(input("Enter Number = "))
check = num
temp = num
count = 0

while temp > 0:
    count+=1
    temp = temp // 10

if count%2 == 0:
    half = count // 2

    divisor = 1
    i = 0
    while i < half:
        divisor = divisor * 10
        i += 1

    first = num // divisor
    second = num % divisor
    print("First Half = ",first)
    print("Second Half = ",second)
    sum = first + second
    print("Sum = ",sum)
    sq = sum**2
    print("Square = ",sq)
if sq == check:
    print("Tech Number")
else:
    print("Not a Tech Number")

