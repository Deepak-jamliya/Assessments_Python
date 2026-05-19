'''
4.
Employee ID Validator

A company wants to validate employee IDs before storing them in the database.

Conditions:
- ID must start with "EMP"
- Total length should be 8
- Remaining characters should be digits only

Input:
Enter Employee ID: EMP10234

Output:
Valid Employee ID
'''

id = input("Enter Employee ID : ")

valid = True

if len(id) != 8:
    valid = False

elif not id.startswith("EMP"):
    valid = False

elif not id[3:].isdigit():
    valid = False

if valid:
    print("Valid Employee ID")
else:
    print("Not Valid")