'''
5.
=========================================
LIBRARY ISBN MANAGER
=========================================

A library stores unique ISBN numbers of books.

Menu:
1. Add ISBN
2. Remove ISBN
3. Search ISBN
4. Display ISBN List
5. Count Books
6. Exit

Requirements:
- Use Set.
- Duplicate ISBNs are not allowed.

'''

isbn = set()

while True:
    print("\nMenu")
    print("1. Add ISBN")
    print("2. Remove ISBN")
    print("3. Search ISBN")
    print("4. Display ISBN List")
    print("5. Count Books")
    print("6. Exit")

    choice = int(input("Enter Choice = "))
    match choice:
        case 1:
            n = int(input("Enter Number of Books = "))
            for i in range(n):
                num = input("Enter ISBN id = ")
                isbn.add(num)
        case 2:
            id = input("Enter ISBN to remove = ")
            for i in isbn:
                if i == id:
                    isbn.remove(i)
            print("After Remove = ",isbn)
        case 3:
            num = input("Enter isbn of book to search = ")
            for i in isbn:
                if isbn == num:
                    print("Found")
                else:
                    print("Not Found")
        case 4:
            print("\nList of isbn : ")
            for i in isbn:
                print(i)
        case 5:
            print("Number of Books = ",len(isbn))
        case 6:
            print("Exiting Menu")
            break
        case _:
            print("Invalid Choice")
            