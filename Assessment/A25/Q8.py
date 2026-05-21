'''
8.
Find the Second Highest Repeating Character in a String

Social Media Trend Analysis System

A social media company analyzes hashtags and user comments to identify trending 
character patterns.

The analytics team wants a Python program to find the character with the second 
highest frequency in a given string.

This helps detect secondary trending patterns in user activity.

Input:

aaabbbbccddeee

Output:

e

Explanation:

b occurs 4 times → highest
e occurs 3 times → second highest

Condition:

Program should work for both uppercase and lowercase letters.
Spaces should be ignored.
If no second highest frequency exists, print:
Second highest repeating character not found
'''


str = input("Enter String = ")

highest = ""
hcount = 0

for i in str:
    count = 0
    for ch in str:
        if i == ch:
            count+=1

    if count > hcount:
        hcount = count
        highest = i

new = ""
ncount = 0

for ch in str:
    if ch != highest:
        new = new + ch

second = ""
scount = 0

for i in new:
    count = 0
    for ch in new:
        if i == ch:
            count+=1

    if count > scount:
        scount = count
        second = i

if second == "":
    print("Second highest repeating character not found")
else:
    print("Second highest repeating character = ",second)