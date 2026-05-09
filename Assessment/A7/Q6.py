'''
6. Company Bonus Distribution System


A company wants to calculate bonuses for employees based on their years of experience:

* More than 10 years → 20% bonus
* 5 to 10 years → 10% bonus
* 2 to 5 years → 5% bonus
* Less than 2 years → No bonus

Write a Python program to calculate the bonus amount.

Input:
Enter salary: 50000
Enter years of experience: 6

Output:
Bonus Amount: ₹5000
------------------------------------------------------------------------------------------'''

salary = int(input("Enter salary : "))
exp = int(input("Enter years of experience : "))

if exp > 10:
    salary = salary * 0.2
    print("Bonus Amount: ",salary)

elif exp > 5 and exp < 10:
    salary = salary * 0.1
    print("Bonus Amount: ",salary)

elif exp > 2 and exp <5:
    salary = salary * 0.05
    print("Bonus Amount: ",salary)

else:
    print("No Bonus")

