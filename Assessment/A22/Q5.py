'''
5.
Advanced Password Security Checker

A cyber security company wants to verify whether employee passwords are highly secure before 
giving system access.

Conditions: Password must:

Start with an uppercase letter
End with a digit
Contain at least 2 digits
Contain at least 1 special character (@ # $ % & *)
Must not contain spaces
Length should be between 8 and 15 characters

Input: Enter password: Python@45

Output: Secure Password
'''

password = input("Enter Password : ")

scount = 0
special = "@#$%&*"
digit = 0
secure = True

if len(password) < 8 or len(password) > 15:
    secure = False

elif " " in password:
    secure = False

elif not password[0].isupper():
    secure = False

elif not password[-1].isdigit():
    secure = False

else:
    for ch in password:
        if ch.isdigit():
            digit+=1
        if ch in special:
            scount+=1
    if digit < 2 or scount < 1:
        secure = False

if secure:
    print("Secure Password")
else:
    print("Not Secure")
