doctors = []

def add_doc():
    did = int(input("Enter Doctor ID = "))
    dname = input("Enter Doctor Name = ")
    spec = input("Enter Specialization = ")
    exp = int(input("Enter Experience = "))
    fees = float(input("Enter Consultation fees = "))

    doctor = {'doctor_name' : did, 'doctor_name' : dname, 'specialization' : spec, 'experience' : exp, 'fees' : fees}
    doctors.append(doctor)

def display_doctors():
    print("Doctors")
    for i in doctors:
        print(i)