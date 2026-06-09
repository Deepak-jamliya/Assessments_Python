'''
4.
Find common elements in three sorted arrays.
Given three arrays sorted in increasing order. Find the elements that are common in all three 
arrays.
Note: can you take care of the duplicates without using any additional Data Structure?
Example 1:
Input:
n1 = 6; A = {1, 5, 10, 20, 40, 80}
n2 = 5; B = {6, 7, 20, 80, 100}
n3 = 8; C = {3, 4, 15, 20, 30, 70, 80, 120}
Output: 20 80
Explanation: 20 and 80 are the only
common elements in A, B and C.
'''

n1 = int(input("Enter Size of list 1 = "))
n2 = int(input("Enter Size of list 2 = "))
n3 = int(input("Enter Size of list 3 = "))

A = []
B = []
C = []

for i in range(n1):
    A.append(int(input("Enter Element Of list 1 = ")))

for i in range(n2):
    B.append(int(input("Enter Element Of list 2 = ")))

for i in range(n3):
    C.append(int(input("Enter Element Of list 3 = ")))


for i in A:
    if i in B and i in C:
        print(i,end = " ")
