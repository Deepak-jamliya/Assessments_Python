'''
2.

ASSIGNMENT: ONLINE COURSE ENROLLMENT & STUDENT MANAGEMENT SYSTEM

A training institute offers multiple courses such as Python, Java, Full Stack Development, 
Data Science, and React.

Currently, student enrollment details are maintained manually in Excel sheets. As the number of 
students is increasing, the institute wants to develop a Student Management System using Python.

The system should store student records in a nested dictionary where:

Key → Student ID
Value → Dictionary containing student information

Each student record should contain:

Student Name
Course Name
Mobile Number
Fees
City
Sample Data Structure
{
101:{
    "name":"Ajay",
    "course":"Python",
    "mobile":"9876543210",
    "fees":25000,
    "city":"Indore"
},
102:{
    "name":"Ravi",
    "course":"Java",
    "mobile":"9876500000",
    "fees":22000,
    "city":"Bhopal"
}
}
Menu Driven Program

Display the following menu repeatedly until the user chooses Exit.

=========================================
 STUDENT MANAGEMENT SYSTEM
=========================================

1. Add New Student
2. Search Student
3. Update Course
4. Delete Student
5. Display All Students
6. Count Total Students
7. Display Students By Course
8. Display Students By City
9. Find Student Paying Highest Fees
10. Find Student Paying Lowest Fees
11. Exit
Functional Requirements
1. Add New Student

Accept the following details:

Student ID
Student Name
Course Name
Mobile Number
Fees
City

Store the information in the nested dictionary.

Validation

If Student ID already exists:

Student ID Already Exists
2. Search Student

Accept Student ID from the user.

If found, display complete student information.

Sample Output
Student ID : 101
Name       : Ajay
Course     : Python
Mobile     : 9876543210
Fees       : 25000
City       : Indore

If not found:

Student Not Found
3. Update Course

Accept Student ID.

If found:

Ask for new course name.
Update the course.
Sample Output
Course Updated Successfully
4. Delete Student

Accept Student ID.

If found:

Delete the record.
Sample Output
Student Deleted Successfully

Otherwise:

Student Not Found
5. Display All Students

Display all student records in a proper format.

Sample Output
-----------------------------------
Student ID : 101
Name       : Ajay
Course     : Python
Fees       : 25000
-----------------------------------

Student ID : 102
Name       : Ravi
Course     : Java
Fees       : 22000
-----------------------------------
6. Count Total Students

Display total number of students enrolled.

Sample Output
Total Students : 45
7. Display Students By Course

Accept a course name from the user.

Display all students enrolled in that course.

Sample Output
Enter Course : Python

101  Ajay
105  Neha
112  Aman

If no students are found:

No Students Found
8. Display Students By City

Accept city name from the user.

Display all students belonging to that city.

Sample Output
Enter City : Indore

101  Ajay
108  Ravi
115  Pooja
9. Find Student Paying Highest Fees

Display complete details of the student who has paid the highest fees.

Sample Output
Highest Fee Paying Student

Student ID : 121
Name       : Neha
Course     : Data Science
Fees       : 50000
10. Find Student Paying Lowest Fees

Display complete details of the student who has paid the lowest fees.

Sample Output
Lowest Fee Paying Student

Student ID : 131
Name       : Aman
Course     : React
Fees       : 15000
11. Exit

Terminate the application.

Sample Output
Thank You For Using Student Management System
'''


d = {}

while True:
    print("\n1. Add New Student")
    print("2. Search Student")
    print("3. Update Course")
    print("4. Delete Student")
    print("5. Display All Students")
    print("6. Count Total Students")
    print("7. Display Students By Course")
    print("8. Display Students By City")
    print("9. Find Student Paying Highest Fees")
    print("10. Find Student Paying Lowest Fees")
    print("11. Exit")

    choice = int(input("Enter Your Choice = "))
    match choice:
        case 1:
            n = int(input("Enter Number of Students = "))
            for i in range(n):
                id = int(input("Enter Student ID = "))
                if id in d:
                    print("Student Already Exist")
                else:
                    name = input("Enter Student Name = ")
                    course = input("Enter Course Name = ")
                    mob = int(input("Enter Mobile Number = "))
                    fee = float(input("Enter Fees = "))
                    city = input("Enter City = ")
                    d[id] = {"name": name, "course": course, "mob" : mob, "fees" : fee, "city" : city}
                    print("Student Registered successfully")
        case 2:
            id = int(input("Enter ID to Search Student = "))
            if id in d:
                print("Student ID : ",id)
                print("Name       : ",d[id]['name'])
                print("Course     : ",d[id]['course'])
                print("Mobile NO. : ",d[id]['mob'])
                print("Fees       : ",d[id]['fees'])
                print("City       : ",d[id]['city'])
            else:
                print("Student Not Found")
        case 3:
            id = int(input("Enter ID to update Course = "))
            if id in d:
                c = input("Enter Course to update = ")
                d[id]['course'] = c
                print("Course Updated Successfully")
            else:
                print("ID not Found")
        case 4:
            id = int(input("Enter ID to delete Student = "))
            if id in d:
                d.pop(id)
                print("Student data Deleted")
            else:
                print("Student Not Found")
        case 5:
            for i in d:
                print("\nStudent ID = ",i)
                print("Name = ",d[i]['name'])
                print("Course = ",d[i]['course'])
                print("Fees = ",d[i]['fees'])
        case 6:
            count = 0
            for i in d:
                count+=1
            print("Total Students  = ",count)
        case 7:
            c = input("Enter Course Name = ")
            f = 1
            for i in d:
                if d[i]['course'] == c:
                    print(i,d[i]['name'])
                    f = 0
            if f:
                print("Student Not Found")
        case 8:
            c = input("Enter City = ")
            f = 1
            for i in d:
                if d[i]['city'] == c:
                    print(i,d[i]['name'])
                    f = 0
            if f:
                print("Student Not Found")
        case 9:
            max = 0
            for i in d:
                if d[i]['fees'] > max:
                    max = d[i]['fees']
                    id = i
            print("\nHighest Fee Paying Student")
            print("Student ID : ",id)
            print("Name       : ",d[id]['name'])
            print("Course     : ",d[id]['course'])
            print("Fees       : ",d[id]['fees'])
        case 10:
            min = 100000
            for i in d:
                if d[i]['fees'] < min:
                    min = d[i]['fees']
                    id = i
            print("\nLowest Fee Paying Student")
            print("Student ID : ",id)
            print("Name       : ",d[id]['name'])
            print("Course     : ",d[id]['course'])
            print("Fees       : ",d[id]['fees'])
        case 11:
            print("Thank You For Using Student Management System")
            break   
        case _:
            print("Invalid Choice")