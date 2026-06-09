'''
5.

Rearrange the array in alternating positive and negative items
Given an unsorted array Arr of N positive and negative numbers. 
Your task is to create an array of alternate positive and negative numbers 
without changing the relative order of positive and negative numbers.
Note: Array should start with positive number.

Example 1:
Input: 
N = 9
Arr[] = {9, 4, -2, -1, 5, 0, -5, -3, 2}
Output:
9 -2 4 -1 5 -5 0 -3 2
Example 2:
Input: 
N = 10
Arr[] = {-5, -2, 5, 2, 4, 7, 1, 8, 0, -8}
Output:
5 -5 2 -2 4 -8 7 1 8 0
'''

n = int(input("Enter Size of list = "))

arr = []

for i in range(n):
    arr.append(int(input()))

pos = []
neg = []

for i in arr:
    if i >= 0:
        pos.append(i)
    else:
        neg.append(i)

result = []
i = 0
j = 0


while i < len(pos) and j < len(neg):
    result.append(pos[i])
    result.append(neg[j])
    i += 1
    j += 1


while i < len(pos):
    result.append(pos[i])
    i += 1


while j < len(neg):
    result.append(neg[j])
    j += 1

print(result)

