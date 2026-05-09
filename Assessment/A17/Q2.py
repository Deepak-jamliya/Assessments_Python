'''
2. Digit Sum Mirror Checker

A validation system checks symmetry in digit sums.

Write a program to:

Split number into two halves
Find sum of first half digits
Find sum of second half digits
Display both sums
If both sums are equal → print Balanced Number
Else → print Unbalanced Number

Input:
123321

Output:
First Half Sum = 6
Second Half Sum = 6
Balanced Number'''

num = int(input("Enter Number = "))
count = 0
temp = num

while temp > 0:
    count+=1
    temp = temp // 10

half = count//2

first = 0
second = 0

for i in range(half):
    digit = num % 10
    second = second + digit
    num = num // 10

for i in range(half):
    digit = num % 10
    first = first + digit
    num = num // 10

print("First Half Sum = ",first)
print("Second Half Sum = ",second)

if first == second:
    print("Balanced Number")
else:
    print("Unbalanced Number")
