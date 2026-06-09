'''
=====================================================================
QUESTION 1: EMPLOYEE SALARY ANALYSIS
====================================

A company wants to store employee details and generate salary reports using NamedTuple.

Fields:
emp_id, emp_name, department, salary

Requirements:

1. Read N employee details from the user and store them in a list of NamedTuples.

---

2. Display all employee details.

---

3. Find and display the employee with the highest salary.

---

4. Find and display the employee with the lowest salary.

---

5. Calculate and display the average salary of all employees.

---

6. Accept a department name from the user and display all employees belonging to that department.

---

Test Case:

Input:
Enter number of employees: 4

101 Rahul IT 50000
102 Priya HR 45000
103 Amit IT 70000
104 Neha Finance 60000

Enter department: IT

Expected Output:
Highest Salary Employee:
103 Amit IT 70000

Lowest Salary Employee:
102 Priya HR 45000

Average Salary:
56250.0

Employees in IT Department:
101 Rahul IT 50000
103 Amit IT 70000
'''
from collections import namedtuple
n = int(input("Enter Number of Employees = "))

Employee = namedtuple("Employee",["emp_id", "emp_name", "department", "salary"])

data = []

for i in range(n):
    id = int(input(f"Enter Employee {i+1} id = "))
    name = input(f"Enter Employee {i+1} name = ")
    dept = input(f"Enter Employee {i+1} Department = ")
    sal = float(input(f"Enter Employee {i+1} Salary = "))
    data.append(Employee(id,name,dept,sal))

for i in data:
    print(i.emp_id,i.emp_name,i.department,i.salary)

highest = 0
for i in data:
    if i.salary > highest:
        highest = i.salary
print(i.emp_id,i.emp_name,i.department,i.salary)

lowest = data[0].salary
lowest_emp = data[0]

for i in data:
    if i.salary < lowest:
        lowest = i.salary
        lowest_emp = i
print(lowest_emp.emp_id,lowest_emp.emp_name,lowest_emp.department,lowest_emp.salary)