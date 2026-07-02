def generate_bill():
    pid = int(input("Enter Patient ID = "))
    charges = int(input("Enter Consultation Charges = "))
    mcost = int(input("Enter Medicine Cost = "))
    tcharges = int(input("Enter Test Charges = "))

    total = charges + mcost + tcharges

    print("\n-----Bill----")
    print("Patient ID = ",pid)
    print("Consultation Charges = ",charges)
    print("Medicine Cost = ",mcost)
    print("Test Charges = ",tcharges)
    print("Total Bill = ",total)
    


