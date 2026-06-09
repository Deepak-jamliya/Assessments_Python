'''
# 7. Enterprise Password Pattern Strength Analyzer

A cybersecurity company wants to validate advanced passwords.

## Conditions:

* Minimum 10 characters
* At least:

  * 1 uppercase letter
  * 1 lowercase letter
  * 1 digit
  * 1 special character
* No consecutive repeating characters
* No spaces allowed

### Input:

text
Pyth@n1234


### Output:

text
Strong Password


### Input:

text
Paaass@12


### Output:

text
Weak Password
'''

password = input("Enter Password = ")

strong = True

if len(password) < 10:
    strong = False

if " " in password:
    strong = False

upper = lower = digit = special = False

for ch in password:
    if ch.isupper():
        upper = True
    elif ch.islower():
        lower = True
    elif ch.isdigit():
        digit = True
    else:
        special = True

for i in range(len(password) - 1):
    if password[i] == password[i + 1]:
        strong = False
        break

if strong and upper and lower and digit and special:
    print("Strong Password")
else:
    print("Weak Password")