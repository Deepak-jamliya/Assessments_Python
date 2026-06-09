'''
2.
Secure Password Analysis

A cybersecurity team wants to identify pairs of passwords having no common characters.

Problem Statement:

Given N strings, count the number of pairs that do not share any common character.

Example:

Input

N = 4
passwords[] = {"abc", "de", "fg", "ad"}

Output

3

Explanation

("abc","de")
("abc","fg")
("de","fg")
'''

n = int(input("Enter Size of list = "))
passwords = []

for i in range(n):
    passwords.append(input())

count = 0

for i in range(len(passwords)):
    for j in range(i+1, len(passwords)):
        ch = passwords[i]
        for k in ch:
            if k in passwords[j]:
                break
        else:
            count+=1

print(count)