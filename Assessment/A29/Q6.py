'''
6.

A security system logs employee entry IDs during a day.

Only prime-numbered IDs are considered valid VIP entries.

Tasks:

Extract all prime IDs from the list
Find the sum of prime IDs
Find the maximum prime ID
Count how many prime entries exist

Input:
A list of integers (may contain duplicates and non-prime numbers)

Example 1

Input:
[12, 5, 7, 9, 11, 14, 17]

Output:
Prime IDs = [5, 7, 11, 17]
Sum = 40
Max = 17
Count = 4

Example 2

Input:
[4, 6, 8, 10]

Output:
Prime IDs = []
Sum = 0
Max = -1
Count = 0
'''

n = int(input("Enter Size of list : "))

arr = []

for i in range(n):
    arr.append(int(input()))

primeid = []
sum = 0
count = 0

for i in arr:
    isprime = 1
    for j in range(2,i//2+1):
        if i%j == 0:
            isprime = 0
            break
    if isprime:
        primeid.append(i)
        sum+=i
        count+=1

max = -1
for i in primeid:
    if i > max:
        max = i


print("Prime IDs = ",primeid)
print("Sum = ",sum)
print("Max = ",max)
print("Count = ",count)


