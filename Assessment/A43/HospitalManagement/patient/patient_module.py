patients = []

def add_patient():
    n = int(input("Enter Number pf Patients = "))
    for i in range(n):
        pid = int(input("Enter Patient ID = "))
        pname = input("Enter Patient Name = ")
        page = int(input("Enter Patient Age = "))
        gender = input("Enter Patient Gender = ")
        disease = input("Enter Patient Disease = ")
        mob = int(input("Enter Patient Mobile Number = "))

        patient = {'patient_id' : pid, 'patient_name' : pname, 'patient_age' : page, 'gender' : gender, 'disease' : disease, 'Mobile_no' : mob}
        patients.append(patient)

def display_p():
    if patients == []:
        print("No Patients")
    else:
        print("Patients Details")
        for i in patients:
            print(i)

def search():
    id = int(input("Enter ID to Search = "))
    for i in patients:
        if i['patient_id'] == id:
            print("Patient Found")
            print(i)
        else:
            print("Patient Not Found")
