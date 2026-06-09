'''
=====================================================================
QUESTION 2: STUDENT RESULT PROCESSING
=====================================

A training institute wants to manage student records using NamedTuple.

Fields:
roll_no, name, course, marks

Requirements:

1. Read N student records from the user and store them in a list of NamedTuples.

---

2. Display all student details.

---

3. Find and display the topper of the class.

---

4. Count and display the number of students scoring above 80 marks.

---

5. Calculate and display the average marks.

---

6. Accept a course name from the user and display all students enrolled in that course.

---

Test Case:

Input:
Enter number of students: 4

1 Ravi Python 85
2 Anjali Java 78
3 Karan Python 92
4 Pooja Testing 88

Enter course: Python

Expected Output:
Topper:
3 Karan Python 92

Students Above 80:
3

Average Marks:
85.75

Students in Python Course:
1 Ravi Python 85
3 Karan Python 92
'''

from collections import namedtuple
n = int(input("Enter Number of Students = "))
student = namedtuple("student",["roll_no", "name", "course", "marks"])


data = []

for i in range(n):
    r = int(input(f"Enter Roll Number of Student {i+1} = "))
    sname = input(f"Enter Name of Student {i+1} = ")
    c = input(f"Enter Course of Student {i+1} = ")
    m = float(input(f"Enter marks of Student {i+1} = "))
    data.append(student(r,sname,c,m))

for i in range(n):
    print(f"Student {i+1} Details : ")
    print(data[i].roll_no,data[i].name,data[i].course,data[i].marks)

cname = input("Enter Course name = ")
top = data[0].marks
topper = data[0]
count = 0
sum = 0
cnames = []

for i in data:
    if i.marks > top:
        top = i.marks
        topper = i
    if i.marks > 80:
        count+=1
    sum+=i.marks
    if i.course == cnames:
        cnames.append(i)

print("\nTopper:")
print(topper.roll_no,topper.name,topper.course,topper.marks)
print("\nStudents scored above 80 : ")
print(count)
print("\nAverage Marks : ")
print(sum/len(data))
print(f"\nStudents in {cname} Course : ")
for s in cnames:
    print(s.roll_no, s.name, s.course, s.marks)
