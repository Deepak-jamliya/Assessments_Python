import random
from datetime import datetime, timedelta


class Booking:
    def __init__(self, booking_id, customer, room, check_in_date, days):
        self.booking_id = booking_id
        self.customer = customer
        self.room = room
        self.check_in_date = check_in_date
        self.days = days
        self.is_active = True

    def show_booking(self):
        status = "Active" if self.is_active else "Cancelled"
        print(f"Booking ID: {self.booking_id} | Customer: {self.customer.name} | "
              f"Room: {self.room.room_number} | Check-in: "
              f"{self.check_in_date.strftime('%d-%m-%Y')} | Days: {self.days} | "
              f"Check-out: {self.calculate_checkout_date().strftime('%d-%m-%Y')} | "
              f"Status: {status}")

    def calculate_checkout_date(self):
        return self.check_in_date + timedelta(days=self.days)

    def extend_stay(self, extra_days):
        self.days += extra_days

    def cancel_booking(self):
        self.is_active = False
        self.room.vacate_room()

    @classmethod
    def generate_booking_id(cls):
        random_part = random.randint(100, 999)
        timestamp_part = datetime.now().strftime("%H%M%S")
        return f"BK{timestamp_part}{random_part}"
