'''
2.
=========================================
ONLINE COURSE ENROLLMENT SYSTEM
=========================================

An institute offers:
1. Python Course
2. Java Course

Store enrolled student email IDs using sets.

Menu:
1. Enroll Student in Python
2. Enroll Student in Java
3. Display Python Students
4. Display Java Students
5. Find Students Enrolled in Both Courses
6. Find Students Enrolled Only in Python
7. Find Students Enrolled Only in Java
8. Check Enrollment in Python Course
9. Display Total Unique Students
10. Exit

Requirements:
- Use two sets.
- Use membership operator (in).
- Use union, intersection and difference operations.
'''

python = set()
java = set()

while True:
    print("\nMenu")
    print("1. Enroll Student in Python")
    print("2. Enroll Student in Java")
    print("3. Display Python Students")
    print("4. Display Java Students")
    print("5. Find Students Enrolled in Both Courses")
    print("6. Find Students Enrolled Only in Python")
    print("7. Find Students Enrolled Only in Java")
    print("8. Check Enrollment in Python Course")
    print("9. Display Total Unique Students")
    print("10. Exit")

    choice = int(input("Enter Choice = "))
    match choice:
        case 1:
            n = int(input("Enter Number Of Students = "))
            for i in range(n):
                pmail = int(input("Enter Student mail = "))
                python.add(pmail)
        case 2:
            n = int(input("Enter Number Of Students = "))
            for i in range(n):
                jmail = int(input("Enter Student mail = "))
                java.add(jmail)
        case 3:
            for i in python:
                print(i)
        case 4:
            for i in java:
                print(i)
        case 5:
            both = python.intersection(java)
            print("Enrolled in both = ",both)
        case 6:
            only_python = python - java
            print("Only Python = ",only_python)
        case 7:
            only_java = java - python
            print("Only Java = ",only_java)
        case 8:
            id = input("Enter Id to check = ")
            if id in python:
                print("Student is Enrolled in Python")
            else:
                print("Student is not Enrolled in Python")
        case 9:
            total = len(python.union(java))
            print("Total = ",total)
        case 10:
            print("Exiting Menu")
            break
        case _:
            print("invalid Choice")



