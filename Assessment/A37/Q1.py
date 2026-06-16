'''
1.ASSIGNMENT: HOSPITAL PATIENT RECORD MANAGEMENT SYSTEM:--

A multi-specialty hospital is currently maintaining patient records manually in registers. 
As the number of patients is increasing, it has become difficult to search, update, and manage 
records efficiently.

The hospital management has decided to develop a simple Patient Record Management System using 
Python. The system should store patient information in a nested dictionary where:

Key → Patient ID
Value → Dictionary containing patient details

Each patient record should contain:

Patient Name
Age
Gender
Disease
Doctor Name
Sample Data Structure
{
101:{
    "name":"Ajay",
    "age":35,
    "gender":"Male",
    "disease":"Fever",
    "doctor":"Dr. Sharma"
},
102:{
    "name":"Ravi",
    "age":42,
    "gender":"Male",
    "disease":"Diabetes",
    "doctor":"Dr. Gupta"
}
}
Menu Driven Program

Display the following menu repeatedly until the user chooses Exit.

=====================================
 HOSPITAL PATIENT MANAGEMENT SYSTEM
=====================================

1. Add New Patient
2. Search Patient
3. Update Patient Disease
4. Delete Patient Record
5. Display All Patients
6. Count Total Patients
7. Display Patients By Disease
8. Display Oldest Patient
9. Display Youngest Patient
10. Exit

Functional Requirements
1. Add New Patient

Accept the following information from the user:

Patient ID
Patient Name
Age
Gender
Disease
Doctor Name

Store the record in the nested dictionary.

Validation:
If the Patient ID already exists, display:

Patient ID already exists.

2. Search Patient

Accept Patient ID from the user.

If the patient exists, display complete information.

Sample Output

Patient ID : 101
Name       : Ajay
Age        : 35
Gender     : Male
Disease    : Fever
Doctor     : Dr. Sharma

If Patient ID is not found:

Patient Record Not Found

3. Update Patient Disease

Accept Patient ID.

If found:

Ask for new disease.
Update the disease information.

Sample Output

Disease Updated Successfully
4. Delete Patient Record

Accept Patient ID.

If found:

Remove the patient record.

Sample Output

Patient Record Deleted Successfully

Otherwise:

Patient Not Found
5. Display All Patients

Display all patient records in a formatted manner.

Sample Output

--------------------------------
Patient ID : 101
Name       : Ajay
Age        : 35
Disease    : Fever
Doctor     : Dr. Sharma
--------------------------------

Patient ID : 102
Name       : Ravi
Age        : 42
Disease    : Diabetes
Doctor     : Dr. Gupta
6. Count Total Patients

Display the total number of patients currently stored.

Sample Output

Total Patients : 25
7. Display Patients By Disease

Accept a disease name from the user.

Display all patients suffering from that disease.

Sample Output

Enter Disease : Fever

101  Ajay
108  Aman
115  Neha

If no patient is found:

No Patient Found
8. Display Oldest Patient

Find and display the patient having the highest age.

Sample Output

Oldest Patient Details

Patient ID : 110
Name       : Ravi
Age        : 68
Disease    : Diabetes
Doctor     : Dr. Gupta
9. Display Youngest Patient

Find and display the patient having the minimum age.

Sample Output

Youngest Patient Details

Patient ID : 121
Name       : Riya
Age        : 4
Disease    : Viral Fever
Doctor     : Dr. Mehta
10. Exit

Terminate the application.

Sample Output

Thank You For Using Hospital Patient Management System
'''


patients = {}

while True:
    print("\n\nHOSPITAL PATIENT MANAGEMENT SYSTEM")
    print("1. Add New Patient")
    print("2. Search Patient")
    print("3. Update Patient Disease")
    print("4. Delete Patient Record")
    print("5. Display All Patients")
    print("6. Count Total Patients")
    print("7. Display Patients By Disease")
    print("8. Display Oldest Patient")
    print("9. Display Youngest Patient")
    print("10. Exit")

    choice = int(input("Enter Your Choice = "))
    match choice:
        case 1:
            id = int(input("Enter Patient ID = "))
            if id in patients:
                print("Patient ID already exists.")
            else:
                name = input("Enter Patient Name = ")
                age = int(input("Enter Age = "))
                gender = input("Enter Gender = ")
                disease = input("Enter Disease = ")
                doctor = input("Enter Doctor Name = ")

                patients[id] = {"name": name,"age": age,"gender": gender,"disease": disease,"doctor": doctor}
                print("Patient Record Added Successfully")
        case 2:
            pid = int(input("Enter Patient Id to Search = "))
            if pid in patients:
                print("\nPatient name = ",patients[pid]["name"])
                print("Patient age = ",patients[pid]["age"])
                print("Patient gender = ",patients[pid]["gender"])
                print("Patient disease = ",patients[pid]["disease"])
                print("Patient Doctor Name = ",patients[pid]["doctor"])
            else:
                ("Patient Not Found")
        case 3:
            id = int(input("Enter patient id to update disease = "))
            if id in patients:
                dis = input("Enter Disease to Update = ")
                patients[id]["disease"] = dis
            else:
                print("Patient Not Found")
        case 4:
            id = int(input("Enter patient id to update disease = "))
            if id in patients:
                patients.pop(id)
            else:
                print("Patient not found")
        case 5:
            for i in patients:
                print("\n\n--------------------------------")
                print("Patient Id   :  ",id)
                print("Name         :  ",patients[id]["name"])
                print("Patient age = ",patients[id]["age"])
                print("Patient gender = ",patients[id]["gender"])
                print("Patient disease = ",patients[id]["disease"])
                print("Patient Doctor Name = ",patients[id]["doctor"])
                print("--------------------------------")
        case 6:
            count = 0
            for i in patients:
                count+=1
            print("Number of Patients = ",count)
        case 7:
            dis = input("Enter Disease = ")
            for i in patients:
                if patients[i]["disease"] == dis:
                    print(patients[id],patients["name"])
        case 8:
            max = 0
            for i in patients:
                if patients[i]["age"] > age:
                    max= patients[i]["age"]
                    id = i
            print("\nOldest Patient Details")
            print("Patient Id   :  ",id)
            print("Name         :  ",patients[id]["name"])
            print("Patient age = ",patients[id]["age"])
        case 9:
            min = 100
            for i in patients:
                if patients[i]["age"] < min:
                    min= patients[i]["age"]
                    id = i
            print("\nYoungest Patient Details")
            print("Patient Id   :  ",id)
            print("Name         :  ",patients[id]["name"])
            print("Patient age = ",patients[id]["age"])
        case 10:
            print("Thank You For Using Hospital Patient Management System")
            break
        case _:
            print("Invalid Choice")





