

total = 0

pizza = 0
fries = 0
chocolate_chai = 0
maggie = 0
hot_chocolate = 0
burger = 0
chocolate_shake = 0

while True:
    print("\n\n--------------- SMART CAFE ---------------")
    print("\n             1 - View Menu")
    print("             2 - Order Item")
    print("             3 - Generate Bill")
    print("             4 - Check Discount")
    print("             5 - Exit")

    choice = int(input("Enter Choice = "))

    match choice:
        case 1:
            print("1) Pizza            ----------  150/-")
            print("2) Fries            ----------  99/-")
            print("3) Chocolate Chai   ----------  30/-")
            print("4) Maggie           ----------  49/-")
            print("5) Hot Chocolate    ----------  110/-")
            print("6) Burger           ----------  129/-")
            print("7) Chocolate Shake  ----------  110/-")
            print("8) Complete Order")
        
        case 2:
            while True:
                item = int(input("Enter Item to Order From MENU and 8 to check out = "))
                match item:
                    case 1:
                        pizza+=1
                        total+=150
                        print("Pizza Added")
                    case 2:
                        fries+=1
                        total+=99
                        print("Fries Added")
                    case 3:
                        chocolate_chai+=1
                        total+=30
                        print("Chocolate Chai Added")
                    case 4:
                        maggie+=1
                        total+=49
                        print("Maggie Added")
                    case 5:
                        hot_chocolate+=1
                        total+=110
                        print("Hot Chocolate Added")
                    case 6:
                        burger+=1
                        total+=129
                        print("Burger Added")
                    case 7:
                        chocolate_shake+=1
                        total+=110
                        print("Chocolate Shake Added")
                    case 8:
                        print("Order Confirmed")
                        break
                    case _:
                        print("Invalid Choice")
        case 3:
            if total==0:
                print("No Items are Selected (Empty Cart)")
            else:
                print("\n\n--------------- Bill ---------------")
                if pizza > 0:
                    print("Pizza           --------------  ",pizza," x 150 =",pizza * 150,"/-")
                if fries > 0:
                    print("Fries           --------------  ",fries," x 99 =",fries * 99,"/-")
                if chocolate_chai > 0:
                    print("Chocolate Chai  --------------  ",chocolate_chai," x 30 =",chocolate_chai * 30,"/-")
                if maggie > 0:
                    print("Maggie          --------------  ",maggie," x 49 =",maggie * 49,"/-")
                if hot_chocolate > 0:
                    print("Hot Chocolate   --------------  ",hot_chocolate," x 110 =",hot_chocolate * 110,"/-")
                if burger > 0:
                    print("Burger          --------------  ",burger," x 129 =",burger * 129,"/-")
                if chocolate_shake > 0:
                    print("Chocolate Shake --------------  ",chocolate_shake," x 110 =",chocolate_shake * 110,"/-")
                print("Total Bill      --------------             ",total,"/-")
        case 4:
            if total==0:
                print("No items are added")
            else:
                premium = input("Are you a premium customer (yes/no): ")
                if total > 550:
                    if premium == "yes":
                        discount = total * 20/100
                        ftotal = total - discount
                        print("Final Discounted Price = ",round(ftotal))
                    else:
                        discount = total * 10/100
                        ftotal = total - discount
                        print("Final Discounted Price = ",round(ftotal))
                else:
                    print("No discount for total below 550 add More")
        case 5:
            print("Thank you For Ordering ")
            print("Visit Again!!")
            break
        case _:
            print("Invalid Choice")