'''
5. Find the Number of Unique Characters in a String

Password Strength Analyzer

A cybersecurity company checks password strength based on the number of unique 
characters present.

Passwords containing more unique characters are considered more secure.

Write a Python program to count the number of unique characters in a string.

Input:

aabbccdde

Output:

5
'''

str = input("Enter Password = ")

check = ""
count = 0

i = 0
while i < len(str):
    if str[i] not in check:
        check = check + str[i]
        count+=1
    i+=1

print("Number of Unique Characters = ",count)