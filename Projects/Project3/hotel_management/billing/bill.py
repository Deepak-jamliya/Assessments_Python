import math

class Bill:
    DEFAULT_GST = 12

    def __init__(self, booking, gst_percent=None, discount=0):
        self.booking = booking
        self.gst_percent = gst_percent if gst_percent is not None else Bill.get_gst_rate()
        self.discount = discount

    def calculate_room_cost(self):
        return self.booking.room.price * self.booking.days

    def calculate_gst(self):
        room_cost = self.calculate_room_cost()
        gst_amount = room_cost * (self.gst_percent / 100)
        return math.ceil(gst_amount)

    def apply_discount(self):
        room_cost = self.calculate_room_cost()
        discount_amount = room_cost * (self.discount / 100)
        return math.floor(discount_amount)

    def total_amount(self):
        room_cost = self.calculate_room_cost()
        gst = self.calculate_gst()
        discount = self.apply_discount()
        total = room_cost + gst - discount
        return math.ceil(total)

    def show_bill(self):
        print("-" * 45)
        print(f"BILL RECEIPT - Booking ID: {self.booking.booking_id}")
        print("-" * 45)
        print(f"Customer      : {self.booking.customer.name}")
        print(f"Room Number   : {self.booking.room.room_number}")
        print(f"Room Type     : {self.booking.room.room_type}")
        print(f"Price/Night   : ₹{self.booking.room.price}")
        print(f"No. of Days   : {self.booking.days}")
        print(f"Room Cost     : ₹{self.calculate_room_cost()}")
        print(f"GST ({self.gst_percent}%)     : ₹{self.calculate_gst()}")
        print(f"Discount ({self.discount}%) : ₹{self.apply_discount()}")
        print(f"TOTAL AMOUNT  : ₹{self.total_amount()}")
        print("-" * 45)

    @staticmethod
    def get_gst_rate():
        return Bill.DEFAULT_GST
