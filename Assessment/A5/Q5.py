'''
5. Banking Security System
   A bank validates login attempt:

* If username is "admin" → Valid user
* If password length ≥ 8 → Strong password

Input:
Enter username: admin
Enter password: secure123

Output:
Valid user
Strong password
-------------------------------------------------------------------'''

name = input("Enter user name : ")
password = input("Enter password : ")

if(name == "admin"):
    print("Valid user")

if(len(password) >= 8):
    print("Strong Password")