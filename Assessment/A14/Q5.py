'''
5.Number Stability Analyzer

A science lab studies whether digits are in increasing order.

Write a program using for-else loop:

- If every next digit is greater than previous print Stable Number
- Else Unstable Number

Input:
12359

Output:
Stable Number'''

num = int(input("Enter Number = "))

curr = 0
prev = 0

for i in range(0,len(str(num))):
    digit = num % 10
    prev = digit
    num = num // 10
    digit = num % 10
    curr = digit
    if curr > prev:
        continue
    print("Stable Number")
    break
else:
    print("Unsatable Number")
