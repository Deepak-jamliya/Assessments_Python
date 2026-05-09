'''
4.Digit Gap Analyzer

A system analyzes the gap between consecutive digits.

Write a program to:

Traverse digits from left to right
Find the absolute difference between current digit and next digit
Display each difference
Count how many differences are greater than 2
Find the maximum difference
If all differences ≤ 2 → print Smooth Number
Else → print Irregular Pattern

Input:
86421
12468

Output:
Differences: 2 2 2 1
Count (>2) = 0
Max Difference = 2
Smooth Number'''

num = int(input("Enter Number = "))
rev = 0
count = 0
max = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

curr = rev % 10
rev = rev // 10

print("Differences = ",end = " ")
while rev > 0:
    next = rev % 10
    diff = abs(curr - next)
    print(diff, end = " ")
    if diff > 2:
        count+=1
    if diff > max:
        max = diff
    curr = next
    rev = rev // 10
print("\nCount(>2) = ",count)
print("Max Difference = ",max)

if count == 0:
    print("Smooth Number")
else:
    print("Irregular Pattern")
