'''
1.
=========================================
STUDENT CLUB MEMBERSHIP SYSTEM
=========================================

A college has two clubs:
1. Coding Club
2. Robotics Club

Store student IDs of both clubs using sets.

Menu:
1. Add Student to Coding Club
2. Add Student to Robotics Club
3. Display Students in Coding Club
4. Display Students in Robotics Club
5. Find Students in Both Clubs
6. Find Students Only in Coding Club
7. Find Students Only in Robotics Club
8. Display All Unique Club Members
9. Display Total Unique Club Members
10. Exit

Requirements:
- Use two sets.
- Apply intersection, difference, and union operations.
'''

coding = set()
robotics = set()

while True:
    print("\nMenu")
    print("1. Add Student to Coding Club")
    print("2. Add Student to Robotics Club")
    print("3. Display Students in Coding Club")
    print("4. Display Students in Robotics Club")
    print("5. Find Students in Both Clubs")
    print("6. Find Students Only in Coding Club")
    print("7. Find Students Only in Robotics Club")
    print("8. Display All Unique Club Members")
    print("9. Display Total Unique Club Members")
    print("10. Exit")

    choice = int(input("Enter Choice = "))
    match choice:
        case 1:
            n = int(input("Enter Number Of Students = "))
            for i in range(n):
                sid = int(input("Enter Student id = "))
                coding.add(sid)
        case 2:
            n = int(input("Enter Number Of Students = "))
            for i in range(n):
                sid = int(input("Enter Student id = "))
                robotics.add(sid)
        case 3:
            for i in coding:
                print(i)
        case 4:
            for i in robotics:
                print(i)
        case 5:
            both = coding.intersection(robotics)
            print(both)
        case 6:
            only_coding = coding - robotics
            print(only_coding)
        case 7:
            only_robotics = robotics - coding
            print(only_robotics)
        case 8:
            unique = coding.union(robotics)
            print(unique)
        case 9:
            total = len(coding.union(robotics))
            print(total)
        case 10:
            print("Exiting Program")
            break
        case _:
            print("Invalid Choice")

