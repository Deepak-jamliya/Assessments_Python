'''
3.
Replace Consecutive Duplicate Characters with Single Character
Data Compression System

A cloud storage company wants to reduce unnecessary repeated characters in text logs.

Write a Python program that replaces consecutive duplicate characters with a single occurrence.

Input:
aaabbbccccdddaa
Output:
abcda
'''

str = input("Enter String = ")

prev = ""
for ch in str:
    prev = ""
    if ch in prev:
        continue
    else:
        prev = ch
print(prev)