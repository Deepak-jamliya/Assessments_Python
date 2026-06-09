'''
3. Missing Number Detector
==========================

Scenario

Numbers from 1 to N should exist in a sequence, but one number is missing.

Requirements

* Read N and list elements from user
* Find the missing number
* Assume numbers belong to the range 1 to N+1

Test Case 1

Input:
[1, 2, 3, 5]

Output:
Missing Number = 4

Test Case 2

Input:
[2, 3, 4, 5]

Output:
Missing Number = 1

Test Case 3

Input:
[1, 2, 4, 5]

Output:
Missing Number = 3
'''

n = int(input("Enter Size of list = "))

arr = []

for i in range(n):
    arr.append(int(input()))
found = 0

for i in range(n):
    if arr[i] != i+1:
        found = 1
        print("Missing Number = ",i+1)
        break

