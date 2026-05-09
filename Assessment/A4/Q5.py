'''Assignment 5: Salary Breakdown

An employee wants to calculate salary per day and per hour.

Input:
Monthly salary = 36000
Working days = 24
Working hours per day = 8

Expected Output:
Salary per day = 1500.0
Salary per hour = 187.5
---------------------------------------------------------------------------------------'''


salary = int(input("Enter your monthly salary : "))
days = int(input("Enter working days : "))
hrs = int(input("Enter working hours per day : "))

perday = salary/days
perhrs = perday/hrs

print(f"Salary per day = {perday}\nSalary per hour = {perhrs}")
