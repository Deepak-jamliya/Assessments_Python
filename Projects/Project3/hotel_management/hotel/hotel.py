from datetime import datetime

from .room import Room
from .customer import Customer


class Hotel:
    def __init__(self, hotel_name):
        self.hotel_name = hotel_name
        self.rooms = []
        self.customers = []
        self.bookings = []

    def add_room(self, room_number, room_type, price):
        if self.find_room_by_number(room_number):
            print(f"Room {room_number} already exists.")
            return None
        room = Room(room_number, room_type, price)
        self.rooms.append(room)
        print(f"Room {room_number} added successfully.")
        return room

    def show_all_rooms(self):
        if not self.rooms:
            print("No rooms found in the hotel.")
            return
        print(f"\n--- All Rooms in {self.hotel_name} ---")
        for room in self.rooms:
            room.show_room()

    def show_available_rooms(self):
        available = [room for room in self.rooms if room.is_available]
        if not available:
            print("No available rooms right now.")
            return
        print("\n--- Available Rooms ---")
        for room in available:
            room.show_room()

    def find_room_by_number(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                return room
        return None

    def add_customer(self, name, phone):
        customer_id = Customer.generate_customer_id()
        customer = Customer(customer_id, name, phone)
        self.customers.append(customer)
        print(f"Customer added successfully. ID: {customer_id}")
        return customer

    def find_customer(self, customer_id):
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer
        print(f"Customer with ID {customer_id} not found.")
        return None

    def show_all_customers(self):
        if not self.customers:
            print("No customers found.")
            return
        print("\n--- All Customers ---")
        for customer in self.customers:
            customer.show_customer()

    def create_booking(self, customer_id, room_number, days, check_in_date=None):
        from booking.booking import Booking

        customer = self.find_customer(customer_id)
        room = self.find_room_by_number(room_number)

        if not customer:
            return None
        if not room:
            print(f"Room {room_number} not found.")
            return None
        if not room.is_available:
            print(f"Room {room_number} is already booked.")
            return None

        if check_in_date is None:
            check_in_date = datetime.now()

        room.book_room()
        customer.assign_room(room_number)

        booking_id = Booking.generate_booking_id()
        booking = Booking(booking_id, customer, room, check_in_date, days)
        self.bookings.append(booking)

        print(f"Booking successful! Booking ID: {booking_id}")
        return booking

    def cancel_booking(self, booking_id):
        booking = self.find_booking(booking_id)
        if not booking:
            print(f"Booking {booking_id} not found.")
            return False
        if not booking.is_active:
            print(f"Booking {booking_id} is already cancelled.")
            return False

        booking.cancel_booking()
        booking.customer.remove_room()
        print(f"Booking {booking_id} cancelled successfully.")
        return True

    def find_booking(self, booking_id):
        for booking in self.bookings:
            if booking.booking_id == booking_id:
                return booking
        return None

    def show_all_bookings(self):
        if not self.bookings:
            print("No bookings found.")
            return
        print("\n--- All Bookings ---")
        for booking in self.bookings:
            booking.show_booking()

    def checkout_customer(self, booking_id):
        booking = self.find_booking(booking_id)
        if not booking:
            print(f"Booking {booking_id} not found.")
            return None
        if not booking.is_active:
            print(f"Booking {booking_id} is not active.")
            return None

        booking.is_active = False
        booking.room.vacate_room()
        booking.customer.remove_room()
        print(f"Customer {booking.customer.name} checked out from Room "
              f"{booking.room.room_number}.")
        return booking


    def show_revenue_report(self):
        """Show a simple revenue summary based on room price x days booked."""
        if not self.bookings:
            print("No bookings yet, nothing to report.")
            return

        total_revenue = 0
        active_count = 0
        cancelled_count = 0

        print("\n--- Hotel Revenue Report ---")
        for booking in self.bookings:
            revenue = booking.room.price * booking.days
            total_revenue += revenue
            if booking.is_active:
                active_count += 1
            else:
                cancelled_count += 1
            status = "Active" if booking.is_active else "Cancelled/Checked-out"
            print(f"Booking {booking.booking_id} | Room {booking.room.room_number} | "
                  f"₹{revenue} | {status}")

        occupied_rooms = sum(1 for room in self.rooms if not room.is_available)
        total_rooms = len(self.rooms)

        print("-" * 40)
        print(f"Total Bookings       : {len(self.bookings)}")
        print(f"Active Bookings      : {active_count}")
        print(f"Cancelled/Checked-out: {cancelled_count}")
        print(f"Occupied Rooms       : {occupied_rooms}/{total_rooms}")
        print(f"Total Revenue        : ₹{total_revenue}")
        print("-" * 40)
