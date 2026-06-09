'''
4. Longest Consecutive Sequence
===============================

Scenario

Find the longest sequence of consecutive numbers present in the list.

Requirements

* Read N and list elements from user
* Find the length of the longest consecutive sequence
* Display the sequence length

Test Case 1

Input:
[100, 4, 200, 1, 3, 2]

Output:
Longest Consecutive Length = 4

Explanation:
Sequence = 1, 2, 3, 4

Test Case 2

Input:
[10, 11, 12, 20]

Output:
Longest Consecutive Length = 3
'''
n = int(input("Enter Size of list = "))

arr = []

for i in range(n):
    arr.append(int(input()))

sarr = sorted(arr)
count = 0
sum = sarr[0]
for i in sarr:
    if i == sum:
        count+=1
    sum+=1

#for i in range(len(sarr)-1):
#   if sarr[i]+1 == sarr[i+1]:
#        count+=1

print("Longest Consecutive Length = ",count)