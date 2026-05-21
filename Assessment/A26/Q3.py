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

new = ""
prev = ""
i = 0
while i < len(str):
    if str[i] != prev:
        prev = str[i]
        new = new + str[i]
    i+=1


print(new)