'''
5. Website URL Verification System

A software company is developing an automated website registration
portal. Before saving a website address, the system must verify whether
the URL follows the required company format.

Conditions: - Must start with www - Must end with .com

Input: Enter website: www.amazon.com

Output: Valid Website
'''

name = input("Enter Website: ")

valid = True

if not name.startswith("www") or not name.endswith(".com"):
    valid = False

if valid:
    print("Valid Website ")
else:
    print("Not a valid Website")

