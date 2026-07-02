from patient import patient_module
from doctor import doctor_module
from appointment import appointment_module
from billing import billing_module


while True:
    print("Menu:")
    print("========== Hospital Management System ==========")
    print("1. Add Patient")
    print("2. Display Patients")
    print("3. Search Patient")
    print("4. Add Doctor")
    print("5. Display Doctors")
    print("6. Book Appointment")
    print("7. Show Appointments")
    print("8. Generate Bill")
    print("9. Exit")

    choice = int(input("Enter Your Choice = "))
    match choice:
        case 1:
            patient_module.add_patient()
        case 2:
            patient_module.display_p()
        case 3:
            patient_module.search()
        case 4:
            doctor_module.add_doc()
        case 5:
            doctor_module.display_doctors()
        case 6:
            appointment_module.app()
        case 7:
            appointment_module.show_appointments()
        case 8:
            billing_module.generate_bill()
        case 9:
            print("Exiting Program")
            break
        case _:
            print("Invalid Choice")














