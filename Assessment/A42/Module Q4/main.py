from customer.c_details import customer,profile
from product.product_details import product,products
from invoice.display_invoice import invoice



while True:
    print("\n----- ONLINE SHOPPING SYSTEM -----")
    print("1. Customer Registration")
    print("2. Product Information")
    print("3. Generate Invoice")
    print("4. Add Multiple Products")
    print("5. Display Customer Profile")
    print("6. Exit")

    choice = int(input("\nEnter Choice : "))
    match choice:
        case 1:
            name = input("Enter Name : ")
            email = input("Enter Email : ")
            mobile = input("Enter Mobile : ")
            customer(name, email, mobile)

        case 2:
            pname = input("Enter Product Name : ")
            price = float(input("Enter Price : "))
            category = input("Enter Category : ")
            product(name=pname, price=price, category=category)

        case 3:
            pname = input("Enter Product Name : ")
            price = float(input("Enter Price : "))
            invoice(pname, price)

        case 4:
            n = int(input("Enter Number of Products : "))
            prices = []
            for i in range(n):
                p = float(input(f"Enter Price {i+1} : "))
                prices.append(p)
            products(*prices)

        case 5:
            name = input("Enter Name : ")
            city = input("Enter City : ")
            email = input("Enter Email : ")
            mobile = input("Enter Mobile : ")
            membership = input("Enter Membership Type : ")
            profile(
            Name=name,
            City=city,
            Email=email,
            Mobile=mobile,
            Membership=membership
            )

        case 6:
            print("\nThank You. Program Terminated.")
            break

        case _:
            print("\nInvalid Choice! Please try again.")