def customer(name, email, mobile):
    print("\nCustomer Registered Successfully")
    print("Name   :", name)
    print("Email  :", email)
    print("Mobile :", mobile)

def profile(**details):
    print("\nCustomer Profile Displayed Successfully")
    for key, value in details.items():
        print(f"{key} : {value}")