appoint = []

def app():
    appid = int(input("Enter Appointment ID = "))
    pid = int(input("Enter patient ID = "))
    did = int(input("Enter Doctor Id = "))
    appdate = input("Enter appointment Date = ")
    apptime = input("Enter Appointment Time = ")

    appointment = {'appoint_id' : appid, 'patient_id' : pid, 'doctor_id' : did, 'appoint_date' : appdate, 'appoint_time' : apptime}
    appoint.append(appointment)

def show_appointments():
    for i in appoint:
        print(i)
        