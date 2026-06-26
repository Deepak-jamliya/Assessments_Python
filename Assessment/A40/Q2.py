'''
2.
Hospital Management System – Oldest Patient

A hospital wants to give priority to the oldest patient during a free health check-up camp. 
The patient details are stored as tuples containing the patient's name and age.

As a Python developer, write a program to identify the oldest patient using the reduce() function 
with a lambda expression.

Input
patients = [
    ("Rahul", 45),
    ("Sneha", 62),
    ("Amit", 38),
    ("Kiran", 71),
    ("Pooja", 55)
]
Expected Output
Oldest Patient: Kiran
'''
from functools import reduce
def main():
    n = int(input("Enter Number of Patients = "))
    patients = []

    for i in range(n):
        name = input(f"Enter Patient {i+1} name = ")
        age = int(input(f"Enter Patient {i+1} age = "))
        patients.append((name,age))

    result = reduce(lambda x,y: x if x[1] > y[1] else y,patients)
    return result[0]

print(main())