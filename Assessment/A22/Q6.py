'''
6.
Railway Ticket PNR Analyzer

A railway department wants to verify whether a PNR number is valid.

Conditions:
- PNR must start with "PNR"
- Total length should be 12 characters
- Remaining characters should be digits

Input:
Enter PNR: PNR123456789

Output:
Valid PNR Number
'''

str = input("Enter PNR = ")

valid = True

if len(str) != 12:
    valid = False

elif not str.startswith("PNR"):
    valid = False

elif not str[3:].isdigit():
    valid = False

if valid:
    print("Valid PNR Number")
else:
    print("Not Valid")

