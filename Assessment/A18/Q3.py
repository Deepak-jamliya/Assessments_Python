'''
3. Employee Bonus Distribution System
A company provides bonuses based on years of experience.
Experience >10 years → 30% bonus
Experience >5 years → 20% bonus
Otherwise → 10% bonus
Write a program to calculate the total salary after adding bonus using inline if.'''

salary = int(input("Enter Salary = "))
exp = int(input("Enter Experience = "))

bonus = 30/100 if exp > 10 else 20/100 if exp > 5 else 10/100

final = salary + (salary * bonus)
print("Final Salary = ",final)