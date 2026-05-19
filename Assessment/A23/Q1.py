'''
1.
Email Username Validator

A company wants to check whether an employee email username is valid before creating an 
official account.

Conditions:
- Username should start with a letter
- Username can contain letters, digits, underscore (_)
- No spaces allowed
- Length should be between 5 and 12 characters

Input:
Enter username: ajay_123

Output:
Valid Username
'''

email = input("Enter Username: ")

valid = True

if len(email) < 5 or len(email) > 12:
    valid = False

elif " " in email:
    valid = False
   
elif not email[0].isalpha():
    valid = False

else:
    for ch in email:
        if not (ch.isalnum() or ch == "_"):
            valid = False
            break

if valid:
    print("Valid Username")
else:
    print("Invalid Username")