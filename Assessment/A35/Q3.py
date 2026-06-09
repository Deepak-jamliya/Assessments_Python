'''
3.
=========================================
WEBSITE VISITOR TRACKING SYSTEM
=========================================

A website stores unique visitor IDs.

Menu:
1. Add Visitor
2. Remove Visitor
3. Check Visitor
4. Display All Visitors
5. Count Unique Visitors
6. Clear Visitor Data
7. Exit

Requirements:
- Use a set to store visitor IDs.
- Duplicate visitor IDs should not be stored.
- Use add(), remove(), and membership operations.
'''

ids = set()

while True:
    print("\nMenu")
    print("1. Add Visitor")
    print("2. Remove Visitor")
    print("3. Check Visitor")
    print("4. Display All Visitors")
    print("5. Count Unique Visitors")
    print("6. Clear Visitor Data")
    print("7. Exit")

    choice = int(input("Enter Choice = "))
    match choice:
        case 1:
            n = int(input("Enter Number Of Students = "))
            for i in range(n):
                id = int(input("Enter Student id = "))
                ids.add(id)
        case 2:
            visit = int(input("Enter Visitor id to remove = "))
            ids.remove(visit)
            print(ids)
        case 3:
            visit = int(input("Enter Visitor id to check = "))
            if visit in ids:
                print("Visitor is present")
            else:
                print("Visitor is not present")
        case 4:
            print("\nList of all visitors")
            for i in ids:
                print(i)
        case 5:
            count = len(ids)
            print("Total Visitors = ",count)
        case 6:
            ids.clear()
            print("Visitor Data is cleared")
        case 7:
            print("Exiting menu")
            break
        case _:
            print("Invalid Choice")