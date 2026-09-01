from datetime import datetime

from hotel.hotel import Hotel
from hotel.customer import Customer
from billing.bill import Bill


def print_menu():
    print("=============================")
    print("HOTEL MANAGEMENT SYSTEM")
    print("=============================")
    print("1.  Add Room")
    print("2.  Show All Rooms")
    print("3.  Show Available Rooms")
    print("4.  Add Customer")
    print("5.  Book Room")
    print("6.  Extend Booking")
    print("7.  Checkout Customer")
    print("8.  Show All Bookings")
    print("9.  Generate Bill")
    print("10. Show Revenue Report")
    print("11. Exit")


def add_room(hotel):
    print("ADD ROOM")
    room_number = input("Enter room number: ").strip()
    room_type = input("Enter room type (Single/Double/Suite): ").strip()
    price = float(input("Enter room price per night: ").strip())
    hotel.add_room(room_number, room_type, price)


def add_customer(hotel):
    print("ADD CUSTOMER")
    name = input("Enter customer name: ").strip()
    phone_choice = input("Auto-generate phone number? (y/n): ").strip().lower()
    if phone_choice == "y":
        phone = Customer.generate_random_phone()
        print(f"Generated phone number: {phone}")
    else:
        phone = input("Enter phone number: ").strip()
    hotel.add_customer(name, phone)


def book_room(hotel):
    print("BOOK ROOM")
    customer_id = input("Enter customer ID: ").strip()
    room_number = input("Enter room number: ").strip()
    days = int(input("Enter number of days to stay: ").strip())
    hotel.create_booking(customer_id, room_number, days, datetime.now())


def extend_booking(hotel):
    print("EXTEND BOOKING")
    booking_id = input("Enter booking ID: ").strip()
    booking = hotel.find_booking(booking_id)
    if not booking:
        print("Booking not found.")
        return
    extra_days = int(input("Enter extra days: ").strip())
    booking.extend_stay(extra_days)
    print(f"Booking {booking_id} extended by {extra_days} day(s).")


def checkout_customer(hotel):
    print("CHECKOUT CUSTOMER")
    booking_id = input("Enter booking ID: ").strip()
    hotel.checkout_customer(booking_id)


def generate_bill(hotel):
    print("GENERATE BILL")
    booking_id = input("Enter booking ID: ").strip()
    booking = hotel.find_booking(booking_id)
    if not booking:
        print("Booking not found.")
        return

    discount_input = input("Enter discount % (or press Enter for 0): ").strip()
    discount = float(discount_input) if discount_input else 0

    bill = Bill(booking, discount=discount)
    bill.show_bill()


def main():
    hotel_name = input("Enter your hotel name: ").strip() or "My Hotel"
    hotel = Hotel(hotel_name)
    print(f"\nWelcome to {hotel.hotel_name}!\n")

    while True:
        print_menu()
        choice = input("Enter your choice (1-11): ")

        if choice == "1":
            add_room(hotel)
        elif choice == "2":
            hotel.show_all_rooms()
        elif choice == "3":
            hotel.show_available_rooms()
        elif choice == "4":
            add_customer(hotel)
        elif choice == "5":
            book_room(hotel)
        elif choice == "6":
            extend_booking(hotel)
        elif choice == "7":
            checkout_customer(hotel)
        elif choice == "8":
            hotel.show_all_bookings()
        elif choice == "9":
            generate_bill(hotel)
        elif choice == "10":
            hotel.show_revenue_report()
        elif choice == "11":
            print("Thank you for using the Hotel Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 11.")

main()
