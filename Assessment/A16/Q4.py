'''
4.
1. Digit Gap Consistency Checker

A number analysis system checks whether the gap between digits follows a consistent pattern.

Write a program to:

Find the absolute difference between first two digits
Compare this difference with all next adjacent digit differences
If any difference is not equal to the first difference, stop using break
Display:
- Initial gap
- Whether all gaps are same or not

Input:
8642

Output:
Initial Gap = 2
Consistent Pattern

Input:
97531

Output:
Initial Gap = 2
Consistent Pattern

Input:
5321

Output:
Initial Gap = 2
Pattern Break Detected'''

num = int(input("Enter Number : "))
check = 0

prev = num % 10
num = num // 10
curr = num % 10
num = num // 10
diff = abs(prev - curr)

while num > 0:
    next = num % 10
    ndiff = abs(curr - next)

    if ndiff != diff:
        check = 1
        break
    curr = next
    num = num // 10
print("Initial Gap = ",diff)

if check:
    print("Pattern Break Detected")
else:
    print("Consistent Pattern")

