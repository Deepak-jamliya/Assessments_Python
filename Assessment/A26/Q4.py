'''
4.

Find All Characters with Maximum Frequency
Website Traffic Analysis System

A web analytics company tracks user activity symbols in server logs.

The company wants to identify all characters having the maximum frequency in the given string.

Input:
aabbbccddd
Output:
b d
'''

str = input("Enter String  ")

char = ""
hcount = 0

for i in str:
    count = 0
    for ch in str:
        if ch == i:
            count+=1
    if count >= hcount:
        hcount = count

for i in str:
    count = 0
    for ch in str:
        if ch == i:
            count+=1
    if count == hcount and i not in char:
        print(i,end = " ")
        char+=i
