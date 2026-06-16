'''
4.
=========================================
STUDENT GRADE ANALYSIS
======================

Store student marks in a dictionary.

students = {
"Ajay":78,
"Ravi":92,
"Neha":85,
"Aman":65
}

Write a program to:

* Find the student with highest marks.
* Find the student with lowest marks.

Sample Output:
Highest Marks : Ravi 92
Lowest Marks : Aman 65
'''

n = int(input("Enter Number of Students = "))

d = {}

for i in range(n):
    key = input(f"Enter Student {i+1} name = ")
    v = int(input(f"Enter Marks of Student {i+1} = "))
    d[key] = v


highest = max(d.values())
lowest = min(d.values())

for name,marks in d.items():
    if marks == highest:
        print("Highest Marks = ",name,marks)
    if marks == lowest:
        print("Lowest Marks = ",name,marks)

