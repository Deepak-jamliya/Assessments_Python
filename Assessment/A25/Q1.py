'''
1. Remove All Special Characters from a String

Online Banking Customer Data Cleaning System

A private bank has launched a new online account opening portal. While entering 
customer details, many users accidentally type unnecessary symbols, emojis, hashtags,
dollar signs, and special characters in their names and addresses.

Before storing the data into the database, the bank wants a Python program that 
removes all unwanted special characters and keeps only:

* Alphabets
* Numbers
* Spaces

The cleaned value should be stored back into the original string variable.

Input:

Deepika@@ Padukone!! 123
Output:
Deepika Padukone 123
Input:
Ajay###Singh$$$
Output:
AjaySingh
'''

str = input("Enter String : ")
result = ""

for ch in str:
    if  ch.isalpha():
        result = result + ch
    elif ch.isdigit():
        result = result + ch
    elif ch == " ":
        result = result + ch

print("Output = ",result)