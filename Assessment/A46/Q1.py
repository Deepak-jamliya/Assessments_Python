'''
ASSIGNMENT 1: Hospital Management System (Single Inheritance)
Scenario
A software company has been hired to develop a Hospital Management System. Every person associated 
with the hospital has some common details, but each category has its own unique information.
Create a base class Person containing:
Person ID
Name
Age
Mobile Number
Create the following derived classes:
Doctor
Specialization
Experience (Years)
Consultation Fee
Nurse
Department
Shift (Day/Night)
Salary
Patient
Disease
Ward Number
Bill Amount
Functional Requirements
Create a menu-driven application.
========== Hospital Management ==========
1. Add Doctor
2. Add Nurse
3. Add Patient
4. Display Doctor Details
5. Display Nurse Details
6. Display Patient Details
7. Exit
Sample Input
Enter Choice : 1

Enter Doctor ID : 101
Enter Name : Rahul Sharma
Enter Age : 45
Enter Mobile : 9876543210
Enter Specialization : Cardiologist
Enter Experience : 18
Enter Consultation Fee : 1500
Sample Output
Doctor Added Successfully

----------- Doctor Details -----------

Doctor ID          : 101
Name               : Rahul Sharma
Age                : 45
Mobile             : 9876543210
Specialization     : Cardiologist
Experience         : 18 Years
Consultation Fee   : ₹1500
'''


class Person:
    def __init__(self, person_id, name, age, mobile_number):
        self.person_id = person_id
        self.name = name
        self.age = age
        self.mobile_number = mobile_number

    def display_person_details(self):
        print(f"Person ID          : {self.person_id}")
        print(f"Name               : {self.name}")
        print(f"Age                : {self.age}")
        print(f"Mobile             : {self.mobile_number}")
class Doctor(Person):
    def __init__(self, person_id, name, age, mobile_number, specialization, experience, consultation_fee):
        super().__init__(person_id, name, age, mobile_number)
        self.specialization = specialization
        self.experience = experience
        self.consultation_fee = consultation_fee

    def display_doctor_details(self):
        self.display_person_details()
        print(f"Specialization     : {self.specialization}")
        print(f"Experience         : {self.experience} Years")
        print(f"Consultation Fee   : ₹{self.consultation_fee}")
class Nurse(Person):
    def __init__(self, person_id, name, age, mobile_number, department, shift, salary):
        super().__init__(person_id, name, age, mobile_number)
        self.department = department
        self.shift = shift
        self.salary = salary

    def display_nurse_details(self):
        self.display_person_details()
        print(f"Department         : {self.department}")
        print(f"Shift              : {self.shift}")
        print(f"Salary             : ₹{self.salary}")

class Patient(Person):
    def __init__(self, person_id, name, age, mobile_number, disease, ward_number, bill_amount):
        super().__init__(person_id, name, age, mobile_number)
        self.disease = disease
        self.ward_number = ward_number
        self.bill_amount = bill_amount

    def display_patient_details(self):
        self.display_person_details()
        print(f"Disease            : {self.disease}")
        print(f"Ward Number        : {self.ward_number}")
        print(f"Bill Amount        : ₹{self.bill_amount}")
while True:
    print("========== Hospital Management ==========")
    print("1. Add Doctor")  
    print("2. Add Nurse")
    print("3. Add Patient")
    print("4. Display Doctor Details")
    print("5. Display Nurse Details")
    print("6. Display Patient Details")
    print("7. Exit")
    choice = input("Enter Choice : ")
    match choice:
        case "1":   
            doctor_id = input("Enter Doctor ID : ")
            name = input("Enter Name : ")
            age = input("Enter Age : ")
            mobile_number = input("Enter Mobile : ")
            specialization = input("Enter Specialization : ")
            experience = input("Enter Experience : ")
            consultation_fee = input("Enter Consultation Fee : ")
            doctor = Doctor(doctor_id, name, age, mobile_number, specialization, experience, consultation_fee)
            print("Doctor Added Successfully")
        case "2":
            nurse_id = input("Enter Nurse ID : ")
            name = input("Enter Name : ")
            age = input("Enter Age : ")
            mobile_number = input("Enter Mobile : ")
            department = input("Enter Department : ")   
            shift = input("Enter Shift (Day/Night) : ")
            salary = input("Enter Salary : ")
            nurse = Nurse(nurse_id, name, age, mobile_number, department, shift, salary)
            print("Nurse Added Successfully")
        case "3":
            patient_id = input("Enter Patient ID : ")
            name = input("Enter Name : ")
            age = input("Enter Age : ")
            mobile_number = input("Enter Mobile : ")
            disease = input("Enter Disease : ")
            ward_number = input("Enter Ward Number : ")
            bill_amount = input("Enter Bill Amount : ")
            patient = Patient(patient_id, name, age, mobile_number, disease, ward_number, bill_amount)
            print("Patient Added Successfully")
        case "4":
            print("----------- Doctor Details -----------")
            doctor.display_doctor_details()
        case "5":
            print("----------- Nurse Details -----------")
            nurse.display_nurse_details()
        case "6":   
            print("----------- Patient Details -----------")
            patient.display_patient_details()
        case "7":
            print("Exiting the program.")
            break
        case _:
            print("Invalid choice. Please try again.")