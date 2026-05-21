'''
3. Find the First Non-Repeated Character

Railway Ticket Fraud Detection System

The railway department generates ticket reference IDs automatically.

Sometimes, due to technical issues, many characters get repeated inside the ticket 
ID.

The department wants a Python program that finds the first character that appears 
only once in the string.

Example 1

Input:
aabbccddefg
Output:


e

'''

str = input("Enter String = ")

flag = 0
i = 0
while i < len(str):
    count = 0
    ch = str[i]
    j = 0
    while j < len(str):
        if ch == str[j]:
            count+=1
        j+=1
    if count == 1:
        print("Non Repeating Character = ",str[i])
        flag = 1
        break
    i+=1
if flag == 0:
    print("No Non Repeating Letter")



