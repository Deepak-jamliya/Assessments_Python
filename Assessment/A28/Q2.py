'''
2.Employee Salary Processing
Store employee salaries in a List and calculate details.

Requirements:

Store salaries
Find average salary
Display salaries greater than average
Remove salaries below 15000

Test Cases:

Input: [10000, 20000, 30000] → Average = 20000, Above Average = 30000
Input: [15000, 15000, 15000] → Average = 15000
Input: [5000, 7000] → Remaining List = []
'''

n = int(input("Enter Size of list : "))

salary = []

for i in range(n):
    x = int(input(f"Enter Salary {i+1} : "))
    salary.append(x)

sum = 0

for i in salary:
    sum = sum + i

avg = sum / n

above = []
for i in salary:
    if i > avg and i > 15000:
        above.append(i)

print(salary)
print("Average : ",avg)
print("Above Average : ",above)
        