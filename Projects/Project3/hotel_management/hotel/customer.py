import random

class Customer:
    def __init__(self, customer_id, name, phone, room_number=None):
        self.customer_id = customer_id
        self.name = name
        self.phone = phone
        self.room_number = room_number

    def show_customer(self):
        room_info = self.room_number if self.room_number else "No room assigned"
        print(f"ID: {self.customer_id} | Name: {self.name} | "
              f"Phone: {self.phone} | Room: {room_info}")

    def assign_room(self, room_number):
        self.room_number = room_number

    def remove_room(self):
        self.room_number = None

    def update_phone(self, new_phone):
        self.phone = new_phone

    @staticmethod
    def generate_customer_id():
        return f"CUST{random.randint(1000, 9999)}"

    @staticmethod
    def generate_random_phone():
        """Generate a random 10-digit Indian-style phone number."""
        first_digit = random.choice(["6", "7", "8", "9"])
        rest = "".join(str(random.randint(0, 9)) for _ in range(9))
        return first_digit + rest
