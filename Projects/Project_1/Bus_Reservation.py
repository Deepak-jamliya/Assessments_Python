
total = 0
dprice = 0

while True:
    print("\n\n--------------- Bus Reservation System ---------------")
    print("1) Bus Type")
    print("2) Routes")
    print("3) Passesnger Category")
    print("4) Generate Ticket")
    print("5) Exit")
    choice = int(input("Enter Your Choice = "))
    match choice:
        case 1:
            print("1) sleeper    ----------  500/-")
            print("2) ac         ----------  700/-")
            print("3) non-ac     ----------  900/-")
            print("4) luxury     ----------  1500/-")

            type = int(input("Enter Bus Type = "))
            match type:
                case 1:
                    total+=500
                    print("Sleeper Bus Booked")
                case 2:
                    total+=700
                    print("AC Bus Booked")
                case 3:
                    total+=900
                    print("Non-AC Bus Booked")
                case 4:
                    total+=1500
                    print("Luxury Bus Booked")
                case _:
                    print("Invalid Bus Type")
        
        case 2:

            print("1) Mumbai to Pune     ----------  500/-")
            print("2) Mumbai to Nashik   ----------  700/-")
            print("3) Indore to Bhopal   ----------  900/-")

            route = int(input("Enter Route = "))
            match route:
                case 1:
                    total+=500
                    print("Mumbai to Pune Route Booked")
                case 2:
                    total+=700  
                    print("Mumbai to Nashik Route Booked")
                case 3:
                    total+=900
                    print("Indore to Bhopal Route Booked")
                case _:
                    print("Invalid Route")
        case 3:
            print("1) Normal         ----------  0% Discount")
            print("2) Student        ----------  10% Discount")
            print("3) Senior Citizen ----------  15% Discount")
            print("4) Military       ----------  20% Discount")
            category = int(input("Enter Passenger Category = "))
            match category:
                case 1:
                    print("Normal Category Selected")
                case 2:
                    dprice = total*0.1
                    print("Student Category Selected")
                case 3:
                    dprice = total*0.15
                    print("Senior Citizen Category Selected")
                case 4:
                    dprice = total*0.2
                    print("Military Category Selected")
                case _:
                    print("Invalid Passenger Category")
        
        case 4:
            if total==0:
                print("Book Ticket First")
            else:
                print("\n\n--------------- Ticket ---------------")
                print("Bus Type = ",type)
                print("Route = ",route)
                print("Passenger Category = ",category)
                print("Total Price = ",total)
                print("Discount = ",dprice)
                print("Amount to Pay = ",total-dprice)
        case 5:
            print("Thank You for Using Bus Reservation System") 
            break
        case _:
            print("Invalid Choice")