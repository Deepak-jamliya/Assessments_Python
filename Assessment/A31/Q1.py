'''
1.
 Second Largest Unique Number
Scenario

A sports academy stores athlete scores in a list.

Find the second largest unique score.

Requirements
Read N and list elements from user
Find second largest unique number
If not available, display a message
Test Case

Input:

[10, 20, 30, 40, 40]

Output:

Second Largest = 30
'''

n = int(input("Enter List Size = "))

arr = []

for i in range(n):
    arr.append(int(input("Enter number =  ")))


result = []
for i in arr:
    if i not in result:
        result.append(i)

sorta = sorted(result)
print("Second Largest",sorta[len(sorta) - 2])