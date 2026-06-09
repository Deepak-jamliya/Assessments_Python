'''
2. First Repeating Number
=========================

Scenario

A security system logs employee IDs.

Find the first ID that repeats in the list.

Requirements

* Read N and list elements from user
* Find the first repeating number
* If no repeating number exists, display an appropriate message

Test Case 1

Input:
[10, 5, 3, 4, 3, 5]

Output:
First Repeating Number = 3

Test Case 2

Input:
[1, 2, 3, 4]

Output:
No Repeating Number Found
'''

n = int(input("Enter Size of list = "))

arr = []

for i in range(n):
    arr.append(int(input()))

check = []
found = 0

for i in arr:
    if i not in check:
        check.append(i)
    else:
        found = 1
        break

if found:
    print("First Repaeting Number = ",i)
else:
    print("No Repeating Number Found")