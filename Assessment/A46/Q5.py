'''
ASSIGNMENT 5: School ERP System (Hierarchical Inheritance)
Scenario
A school is developing an ERP system.
Every person has common information.
Base Class
Person
Name
Age
Address
Derived Classes
Student
Roll Number
Course
Marks
Teacher
Employee ID
Subject
Salary
Principal
Office Number
Experience
Qualification
Functional Requirements
========== School ERP ==========
1. Add Student
2. Add Teacher
3. Add Principal
4. Display Student
5. Display Teacher
6. Display Principal
7. Exit
Sample Input
Choice : 1

Roll Number : 102
Name : Riya Sharma
Age : 20
Address : Indore

Course : Python Full Stack
Marks : 89
Sample Output
----------- Student Details -----------

Roll Number : 102
Name : Riya Sharma
Age : 20
Address : Indore

Course : Python Full Stack
Marks : 89
'''

class Person:
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address
    def display_person(self):
        print("Name = ",self.name)
        print("Age = ",self.age)
        print("Address = ",self.address)

class Student(Person):
    def __init__(self, name, age, address,roll_no,course,marks):
        super().__init__(name, age, address)
        self.roll_no = roll_no
        self.course = course
        self.marks = marks

    def display_student(self):
        print("========== Student Details =======")
        print("Roll No = ",self.roll_no)
        self.display_person()
        print("Course = ",self.course)
        print("Marks = ",self.marks)
    
class Teacher(Person):
    def __init__(self, name, age, address, emp_id, subject, salary):
        super().__init__(name, age, address)
        self.emp_id = emp_id
        self.subject = subject
        self.salary = salary
    def display_teacher(self):
        print("============  Teacher Details ============")
        self.display_person()
        print("Employee ID = ",self.emp_id)
        print("Subject = ",self.subject)
        print("Salary = ",self.salary)

class Principle(Person):
    def __init__(self, name, age, address, office_no, experience, qualification):
        super().__init__(name, age, address)
        self.office_no = office_no
        self.experience = experience
        self.qualification = qualification

    def display_principle(self):
        print("============== Principle Details ==========")
        self.display_person()
        print("Office Nmber = ",self.office_no)
        print("Experience = ",self.experience)
        print("Qualification = ",self.qualification)

while True:
    print("1. Add Student")
    print("2. Add Teacher")
    print("3. Add Principle")
    print("4. Display Student")
    print("5. Display Teacher")
    print("6. Display Principle")
    print("7. Exit")

    choice = int(input("Enter Choice = "))
    match choice:
        case 1:
            roll_no = int(input("Enter Roll no = "))
            name = input("Enter name = ")
            age = int(input("Enter Age = "))
            address = input("Enter Address = ")
            course = input("Enter Course = ")
            marks = int(input("Enter Marks = "))
            s = Student(name,age,address,roll_no,course,marks)
            print("Student Added Successfully")
        case 2:
            name = input("Enter name = ")
            age = int(input("Enter Age = "))
            address = input("Enter Address = ")
            emp_id = int(input("Enter Employee ID = "))
            subject = input("Entter Subject = ")
            salary = float(input("Enter Salary = "))
            teacher  = Teacher(name,age,address,emp_id,subject,salary)
            print("Teacher Added successfully")
        case 3:
            name = input("Enter name = ")
            age = int(input("Enter Age = "))
            address = input("Enter Address = ")
            office_no = int(input("Enter Office Number = "))
            experience = int(input("Enter Experience = "))
            qualification = input("Enter Qualification = ")
            principle = Principle(name,age,address,office_no,experience,qualification)
            print("Principle Added Successfully")
        case 4:
            s.display_student()
        case 5:
            teacher.display_teacher()
        case 6:
            principle.display_principle()
        case 7:
            print("Thank you ")
            break
        case _:
            print("Invalid Choice")
