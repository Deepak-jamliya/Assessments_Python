'''
9.
Step Difference Number Analyzer

A mathematics research center studies hidden patterns inside numbers.
For every entered number, the system compares adjacent digits step by step.

Write a program to:

Find the absolute difference between every pair of adjacent digits
Display all step differences
Find the sum of all step differences
Find the largest step difference
If the sum of step differences is divisible by the number of digits, print Balanced Number
Otherwise print Unbalanced Number

Use loops wherever required.

Input:
57294
Output:
Step Differences: 2 5 7 5
Sum = 19
Largest = 7
Unbalanced Number
'''

# while loop
num = int(input("Enter number: "))

temp = num
digits = 0
while temp > 0:
    digits = digits + 1
    temp = temp // 10

temp = num
prev = temp % 10
temp = temp // 10

total = 0
largest = 0


print("Step Differences:", end=" ")

while temp > 0:
    curr = temp % 10
    diff = abs(prev - curr)

    print(diff, end=" ")

    total = total + diff

    if diff > largest:
        largest = diff

    prev = curr
    temp = temp // 10

print("\nSum =", total)
print("Largest =", largest)

if total % digits == 0:
    print("Balanced Number")
else:
    print("Unbalanced Number")



