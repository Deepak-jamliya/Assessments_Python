'''
1. Adjacent Digit Difference Analyzer

A system analyzes differences between consecutive digits in a number.

Write a program to:

Find the difference between every pair of adjacent digits
Display all differences
Count how many differences are even
Find the largest difference
If all differences are same → print Uniform Difference
Else → print Non-Uniform Pattern

Input:
84261

Output:
Differences: 4 2 4 5
Even Differences Count = 3
Max Difference = 5
Non-Uniform Pattern'''

num = int(input("Enter Number = "))

prev = num % 10
num = num // 10
count = 0
max = 0
check = None
uniform = 1

print("Differences = ",end = " ")
while num > 0:
    curr = num % 10
    diff = abs(curr - prev)
    print(diff, end = " ")
    if diff%2 == 0:
        count+=1
    if diff > max:
        max = diff
    
    if check == None:
        check = diff
    elif diff != check:
        uniform = 0
    prev = curr
    num = num // 10
print("\nEven Digit Count = ",count)
print("Max Difference = ",max)

if uniform:
    print("Unifrom Pattern")
else:
    print("Non Uniform Pattern")
