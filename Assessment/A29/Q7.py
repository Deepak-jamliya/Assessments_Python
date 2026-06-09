'''
7.
Factory Production – Factorial Expansion List

Problem Statement

A factory produces items where production capacity is defined using factorial growth.

Given a list of numbers, replace each number with its factorial value.

Then perform analysis on the resulting list.

Tasks:

Convert each element to factorial
Find sum of all factorial values
Find maximum factorial value
Count how many factorial values are even

Input:
A list of integers

Example 1

Input:
[3, 4, 5]

Processing:
3! = 6
4! = 24
5! = 120

Output:
[6, 24, 120]
Sum = 150
Max = 120
Even Count = 3
'''

n = int(input("Enter Size of list : "))

arr = []

for i in range(n):
    arr.append(int(input()))

factor = []
sum = 0
max = -1
for i in range(n):
    factorial = 1
    for j in range(arr[i],0,-1):
        factorial = factorial * j
    factor.append(factorial)
    sum+=factorial
    if factorial > max:
        max = factorial

count = 0
for i in factor:
    if i%2 == 0:
        count+=1

print(factor)
print("Sum = ",sum)
print("Max = ",max)
print("Count = ",count)
    