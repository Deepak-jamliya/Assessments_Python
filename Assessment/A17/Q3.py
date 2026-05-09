'''
Digit Neighbor Sum Analyzer

A system analyzes the relationship between a digit and its immediate neighbors.

Write a program to:

Traverse digits from left to right (ignore first and last digit)
For each digit, calculate sum of its adjacent digits
Check if current digit is equal to the sum of its neighbors
Display such digits
Count how many such digits exist
If none found → print No Matching Digit
Else → print Neighbor Sum Pattern Found

Input:
121314

Output:
Matching Digits: 2 3
Count = 2
Neighbor Sum Pattern Found'''

num = int(input("Enter Number = "))

rev = 0
temp = num
while temp > 0:
    rev = rev * 10 + (temp % 10)
    temp //= 10

match_count = 0
found = False

print("Matching Digits:", end=" ")

while rev >= 100:
    left = rev % 10
    curr = (rev // 10) % 10
    right = (rev // 100) % 10

    if curr == left + right:
        print(curr, end=" ")
        match_count += 1
        found = True

    rev //= 10 

print("\nCount =", match_count)

if found:
    print("Neighbor Sum Pattern Found")
else:
    print("No Matching Digit")