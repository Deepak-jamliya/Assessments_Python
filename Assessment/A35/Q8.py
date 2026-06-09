'''
8.
=========================================
ALLOWED CHARACTER VALIDATOR
=========================================

Allowed characters are:
A-Z, a-z, 0-9

Store allowed characters in a Frozen Set.

Menu:
1. Enter Username
2. Validate Username
3. Display Allowed Characters
4. Exit

Requirements:
- Use Frozen Set.
- Username should contain only allowed characters.
'''

allowed = frozenset('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')

username = ""

while True:
    print("\nMenu")
    print("1. Enter Username")
    print("2.Validate Username")
    print("3. Display Allowed Characters")
    print("4. Exit")

    choice = int(input("Enter Choice = "))
    match choice:
        case 1:
            user = input("Enter Username = ")
            username = set(user)
        case 2:
            if username.issubset(allowed):
                print("Valid username")
            else:
                print("Invalid Username")
        case 3:
            print("Allowed Characters : ")
            print(allowed)
        case 4:
            print("Exiting Menu")
            break
        case _:
            print("Invalid Choice")
