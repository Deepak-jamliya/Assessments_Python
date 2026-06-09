'''
5. Equilibrium Index Finder
===========================

Scenario

Find an index where:

# Sum of elements on the left side

Sum of elements on the right side

Requirements

* Read N and list elements from user
* Find equilibrium index
* If not found, display message

Test Case 1

Input:
[1, 3, 5, 2, 2]

Output:
Equilibrium Index = 2

Explanation:
1 + 3 = 2 + 2

Test Case 2

Input:
[1, 2, 3]

Output:
No Equilibrium Index Found
'''

n = int(input("Enter List Size = "))
arr = []

for i in range(n):
    arr.append(int(input()))

found = 0
for i in range(n):
    sumleft = 0
    sumright = 0
    for j in range(0,i):
        sumleft+=arr[j]
    for k in range(i+1,n):
        sumright+=arr[k]

    if sumleft == sumright:
        found = 1
        break

if found:
    print("Equilibrium Index = ",i)
else:
    print("No Equilibrium Index")