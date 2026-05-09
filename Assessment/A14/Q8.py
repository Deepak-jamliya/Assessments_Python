'''
8.
 ATM Note Counter

A bank ATM dispenses ₹100 notes.

Write a program to:

- Read withdrawal amount
- Count how many ₹100 notes needed using loop

Input:
700

Output:
Notes = 7'''

num = int(input("Enter Amount = "))


for i in range(0,num):
    hun = num // 100
    rem = num % 100
print("Notes = ",hun)
print("Remaining Amount = ",rem)