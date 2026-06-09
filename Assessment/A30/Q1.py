'''
1. First Non-Repeating Number
   ====================================================================

Scenario

An online voting system stores vote IDs in a list.

Find the first vote ID that appears only once.

Requirements

* Read N and list elements from user
* Find the first non-repeating number
* If no such number exists, display an appropriate message

Test Case 1

Input:
[4, 5, 1, 2, 1, 2, 4]

Output:
First Non-Repeating Number = 5

Test Case 2

Input:
[7, 7, 8, 8]

Output:
No Non-Repeating Number Found
'''

n = int(input("Enter Size of list = "))

voteid = []
check = []

for i in range(n):
    voteid.append(int(input()))

f = 0
for i in voteid:
    count = 0
    for j in voteid:
        if i == j:
            count+=1
    if count == 1:
        f = 1
        break

if f:
    print("First Non Repeating Number = ",i)
else:
    print("No Non Repeating Number")



