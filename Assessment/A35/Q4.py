'''
4.
=========================================
FROZEN SET SUBJECT MANAGEMENT
=========================================

An institute offers fixed subjects:

Python
Java
MySQL
React
Spring Boot

These subjects cannot be modified after creation.

Menu:
1. Display Subjects
2. Search Subject
3. Count Subjects
4. Attempt to Add Subject
5. Exit

Requirements:
- Use Frozen Set.
- Show that modification is not allowed.
'''

subjects = frozenset("Python","Java","Mysql","React","Spring Boot")

while True:
    print("\nMenu")
    print("1. Display Subjects")
    print("2. Search Subjects")
    print("3. Count Subjects")
    print("4. Attempt to add Subjects")
    print("5. Exit")

    choice = int(input("Enter Choice = "))
    match choice:
        case 1:
            for i in subjects:
                print(i)
        case 2:
            sub = input("Enter Subject to Search = ")
            for i in subjects:
                if sub in subjects:
                    print("Subject is Found")
                else:
                    print("Subject is not found")
        case 3:
            print("Total Number of Subjects = ",len(subjects))
        case 4:
            add = input("Enter Subject to add = ")
            subjects.add(add)
        case 5:
            print("Exiting Menu")
            break
        case _:
            print("Invalid Choice")