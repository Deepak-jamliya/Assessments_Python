'''
4.
Palindrome Number List Checker
Scenario

A system checks lucky numbers which are palindromes.

Requirements
Check palindrome numbers
Store palindrome numbers in list
Count palindrome numbers
Find largest palindrome
Sort palindrome list
Test Cases

Input:
[121, 131, 20, 44, 55, 100]

Output:

Palindromes: [121, 131, 44, 55]
Count: 4
Largest: 131
Sorted: [44, 55, 121, 131]
'''

n = int(input("Enter Size of list = "))
arr = []

for i in range(n):
    x = int(input(f"Enter Number {i+1} = "))
    arr.append(x)

palli = []
count = 0
for i in arr:
    if i == int(str(i)[::-1]):
        palli.append(i)
        count+=1
print("Pallindromes = ",palli)
print("Count = ",count)

largest = palli[0]
for i in palli:
    if i > largest:
        largest = i

spalli = sorted(palli)

print("Largest = ",largest)
print("Sorted List = ",spalli)