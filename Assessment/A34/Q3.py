'''
=====================================================================
QUESTION 3: HOSPITAL PATIENT TRACKER
====================================

A hospital stores patient records for daily monitoring.

Fields:
patient_id, patient_name, age, disease

Requirements:

1. Read N patient records from the user and store them in a list of NamedTuples.

---

2. Display all patient details.

---

3. Display patients whose age is above 60 years.

---

4. Search for a patient using Patient ID.

---

5. Count the number of patients suffering from a particular disease.

---

Test Case:

Input:
Enter number of patients: 4

P101 Rajesh 65 Diabetes
P102 Suman 45 Fever
P103 Mohan 70 Diabetes
P104 Rita 35 Cold

Enter Patient ID: P103
Enter Disease: Diabetes

Expected Output:
Patient Found:
P103 Mohan 70 Diabetes

Patients Above 60:
P101 Rajesh 65 Diabetes
P103 Mohan 70 Diabetes

Patients with Diabetes:
2
'''

from collections import namedtuple

n = int(input("Enter Number of Patients = "))
patient = namedtuple("patient",["patient_id", "patient_name", "age", "disease"])

data = []

for i in range(n):
    pid = input(f"Enter Patient {i+1} id = ")
    pname = input(f"Enter Patient {i+1} name = ")
    page = int(input(f"Enter Patient {i+1} age = "))
    pd = input(f"Enter Patient {i+1} Disease = ")
    data.append(patient(pid,pname,page,pd))

print("\nPatient Details : ")
for i in data:
    print(i.patient_id,i.patient_name,i.age,i.disease)

print("\nPatients Above 60:")
for i in data:
    if i.age > 60:
        print(i.patient_id,i.patient_name,i.age,i.disease)

id = input("\nEnter Patient Id = ")
d = input("Enter Disease : ")
count = 0

for i in data:
    if i.patient_id == id:
        print("\nPatient Found : ")
        print(i.patient_id,i.patient_name,i.age,i.disease)
    if i.disease == d:
        count+=1

print(f"\nPatients with {d} : ")
print(count)
