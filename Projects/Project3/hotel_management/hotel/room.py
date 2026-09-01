class Room:
    def __init__(self, room_number, room_type, price, is_available=True):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.is_available = is_available

    def show_room(self):
        status = "Available" if self.is_available else "Booked"
        print(f"Room No: {self.room_number} | Type: {self.room_type} | "
              f"Price: ₹{self.price}/night | Status: {status}")

    def book_room(self):
        if self.is_available:
            self.is_available = False
            return True
        return False

    def vacate_room(self):
        self.is_available = True

    def change_price(self, new_price):
        self.price = new_price

    def mark_available(self):
        self.is_available = True

    def mark_unavailable(self):
        self.is_available = False
