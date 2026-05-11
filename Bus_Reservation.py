
total = 0
dprice = 0
route = ""
customer = ""
bus = ""

while True:
    print("\n\n---------- MENU ----------")
    print("       1. View Bus Types")
    print("       2. Select Route")
    print("       3. Passenger Category")
    print("       4. Generate Ticket")
    print("       5. Exit")

    choice = int(input("Enter Choice = "))
    match choice:
        case 1:
            print("Bus Type           Price")
            print("sleeper ---------- 800/-")
            print("ac      ---------- 1000/-")
            print("non-ac  ---------- 600/-")
            print("luxury  ---------- 1500/-\n")

            bus = input("Enter Bus type : ").lower()
            if bus == "sleeper":
                total = 800
                print("Sleeper seat is selected")
            elif bus == "ac":
                total = 1000
                print("ac seat is selected")
            elif bus == "non-ac":
                total = 600
                print("non-ac seat is selected")
            elif bus == "luxury":
                total = 1500
                print("luxury seat is selected")
            else:
                print("Invalid Bus Type")

        case 2:
            print("Route                    Extra Charge")
            print("1. Bhopal -> Indore ---------- 200/-")
            print("2. Delhi -> Jaipur ---------- 300/-")
            print("3. Mumbai -> pune ---------- 150/-\n")
            route = int(input("Enter Route as 1,2,3 = " ))
            match route:
                case 1:
                    total+=200
                    route = "Bhopal To Indore"
                    print("Bhopal to Indore Route selected")
                case 2:
                    total+=300
                    route = "Delhi To Jaipur"
                    print("Delhi to Jaipur Route selected")
                case 3:
                    total+=150
                    route = "Mumbai To Pune"
                    print("Mumbai to Pune Route selected")
                case _:
                    print("Enter Valid Route")
        case 3:
            print("Enter passenger Category\n1. Student\n2. Senior Citizen\n3. Military\n4. Normal")
            customer = int(input("Enter Passenger type = "))
            if customer == 1:
                customer = "Student"
                discount = total * 10/100
            elif customer == 2:
                customer = "Senior Citizen"
                discount = total * 20/100
            elif customer == 3:
                customer = "Military"
                discount = total * 25/100
            elif customer == 4:
                customer = "Normal"
                discount = 0
            else:
                print("Invalid Customer Type")
            dprice = total - discount
        case 4:
            if dprice == 0 and route == "" and bus == "" and customer == "":
                print("Book Ticket First")
            else:
                print("\n---------- Bus Ticket ----------")
                print("Bus Type             ---------- ",bus)
                print("Route                ---------- ",route)
                print("Passenger Category   ----------",customer)
                print("Total Fare           ----------",dprice)
        case 5:
            if total > 0:
                print("Thank you for booking ticket \nVisit Again")
                break
            else:
                print("Thank you for visiting the site")
                break
        case _:
            print("Please Enter Valid Choice")

