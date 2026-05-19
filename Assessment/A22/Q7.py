'''
7.
Vehicle Number Plate Checker

The traffic department wants to validate vehicle registration numbers.

Conditions:
- First 2 characters should be alphabets
- Next 2 should be digits
- Total length should be 10

Input:
Enter vehicle number: MP04AB1234

Output:
Valid Vehicle Number
'''

num = input("Enter vehicle number = ")

valid = True

if len(num) != 10:
    valid = False

elif not num[0:2].isalpha():
    valid = False

elif not num[2:4].isdigit():
    valid = False

elif not num[4:].isalnum():
    valid = False

if valid:
    print("VALID VEHICLE NUMBER")
else:
    print("Not a Valid Vehicle Number")