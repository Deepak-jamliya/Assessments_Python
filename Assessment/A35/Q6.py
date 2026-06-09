'''
6.

=========================================
COMMON CHARACTER FINDER
=========================================

Enter two strings and find common characters.

Menu:
1. Enter First String
2. Enter Second String
3. Display Common Characters
4. Count Common Characters
5. Exit

Example:
String1: python
String2: typhoon

Output:
{p, t, h, o, n}
'''

s1 = set()
s2 = set()

while True:
    print("\nMenu")
    print("1. Enter First String")
    print("2. Enter Second String")
    print("3. Display Common Characters")
    print("4. Count Common Characters")
    print("5. Exit") 

    choice = int(input("Enter Choice = "))
    match choice:
        case 1:
            s = input("Enter String 1 = ")
            for i in s:
                s1.add(i)
        case 2:
            s = input("Enter String 2 = ")
            for i in s:
                s2.add(i)
        case 3:
            print("Common Characters = ")
            print(s1.intersection(s2))
        case 4:
            print("Number of common Characters : ")
            print(len(s1.intersection(s2)))  
        case 5:
            print("Exiting Menu")
            break
        case _:
            print("Invalid Choice")

