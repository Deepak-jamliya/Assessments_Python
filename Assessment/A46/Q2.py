'''
ASSIGNMENT 2: Employee Payroll Management System (Method Overriding + Menu Driven)
Scenario
An IT company has three categories of employees.
Create a base class Employee.
Common Details
Employee ID
Name
Department
Derived Classes
FullTimeEmployee
Monthly Salary
Bonus
Salary Formula
Salary = Monthly Salary + Bonus
PartTimeEmployee
Hourly Rate
Total Hours Worked
Salary Formula
Salary = Hourly Rate × Hours
ContractEmployee
Project Name
Contract Amount
Salary Formula
Salary = Contract Amount
Functional Requirements
========== Payroll System ==========

1. Add Full Time Employee
2. Add Part Time Employee
3. Add Contract Employee
4. Display Full Time Salary
5. Display Part Time Salary
6. Display Contract Salary
7. Exit
Sample Input
Choice : 2

Employee ID : 205
Name : Aman Verma
Department : Testing

Hourly Rate : 350
Hours Worked : 160
Sample Output
Employee Added Successfully

Employee ID : 205
Name : Aman Verma
Department : Testing

Hourly Rate : 350
Hours Worked : 160

Total Salary : ₹56000
'''

class Employee:
    def __init__(self,emp_id,name,dept):
        self.emp_id = emp_id
        self.name = name
        self.dept = dept
    def display_person(self):
        print("Employee ID = ",self.emp_id)
        print("Name = ",self.name)
        print("Department = ",self.dept)

class FullTime(Employee):
    def __init__(self, emp_id, name, dept, msalary, bonus):
        super().__init__(emp_id, name, dept)
        self.msalary = msalary
        self.bonus = bonus
        self.salary = msalary + bonus
    def display_fulltime(self):
        print("========== Full Time Employee ==========")
        self.display_person()
        print("Monthly Salary = ",self.msalary)
        print("Bonus = ",self.bonus)
        print("Total Salary = ",self.salary)

class PartTimeEmployee(Employee):
    def __init__(self, emp_id, name, dept, hourly_rate, total_hrs):
        super().__init__(emp_id, name, dept)
        self.hourly_rate = hourly_rate
        self.total_hrs = total_hrs
        self.salary = hourly_rate * total_hrs
    def display_parttime(self):
        print("========== Part Time Employee ==========")
        self.display_person()
        print("Hourly Rate = ",self.hourly_rate)
        print("Total Hours = ",self.total_hrs)
        print("Total Salary = ",self.salary)

class ContractEmployee(Employee):
    def  __init__(self, emp_id, name, dept, project_name, contract_amount):
        super().__init__(emp_id, name, dept,)
        self.project_name = project_name
        self.salary = contract_amount
    def display_contract(self):
        print("========== Contract Employee ==========")
        self.display_person()
        print("Project Name = ",self.project_name)
        print("Contract Amount = ",self.salary)


while True:
    print("\n========== Payroll System ==========")
    print("1. Add Full Time Employee")
    print("2. Add Part Time Employee")
    print("3. Add Contract Employee")
    print("4. Display Full Time Employee")
    print("5. Display Part Time Employee")
    print("6. Display Contract Employee")
    print("7. Exit")

    choice = int(input("Enter Your Choice = "))
    match choice:
        case 1:
            id = int(input("Enter Employee ID = "))
            name = input("Enter Employee Name = ")
            dept = input("Enter Employee Department = ")
            msalary = float(input("Enter Employee Monthly Salary = "))
            bonus = float(input("Enter Employee Bonus"))
            fulltime = FullTime(id,name,dept,msalary,bonus)
            print("Full Time Employee Added Successfully")
        case 2:
            id = int(input("Enter Employee ID = "))
            name = input("Enter Employee Name = ")
            dept = input("Enter Employee Department = ")
            hourly_rate = float(input("Enter Hourly Rate = "))
            total_hrs = float(input("Enter Total Hours = "))
            parttime = PartTimeEmployee(id,name,dept,hourly_rate,total_hrs)
            print("Part Time Employee Added Successfully")
        case 3:
            id = int(input("Enter Employee ID = "))
            name = input("Enter Employee Name = ")
            dept = input("Enter Employee Department = ")
            project_name = input("Enter Project Name = ")
            contract_amount = float(input("Enter Contract Amount = "))
            contract = ContractEmployee(id, name, dept, project_name, contract_amount)
            print("Contract Employee Added Successfully")
        case 4:
            fulltime.display_fulltime()
        case 5:
            parttime.display_parttime()
        case 6:
            contract.display_contract()
        case 7:
            print("Thank You for using this System")
            break
        case _:
            print("Invalid Choice")