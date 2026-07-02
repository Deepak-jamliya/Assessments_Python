'''
Question 5: Hotel Room Booking System
Scenario

A hotel wants to generate the final bill of guests based on the duration of their stay.

Requirements

Create a class named Guest with:

guest_id
guest_name
number_of_days
room_charge_per_day

Initialize the values using a constructor.

Calculations
Room Bill = Number of Days × Room Charge Per Day
GST = 12% of Room Bill
Final Bill = Room Bill + GST
Sample Input
Enter Guest ID : G101
Enter Guest Name : Rohan Mehta
Enter Number of Days : 4
Enter Room Charge Per Day : 2500
Sample Output
------ Hotel Bill ------
Guest ID              : G101
Guest Name            : Rohan Mehta
Number of Days        : 4
Room Charge Per Day   : ₹2500.0
Room Bill             : ₹10000.0
GST (12%)             : ₹1200.0
Final Bill            : ₹11200.0
'''

class guest:
    def __init__(self,id,name,days,charge):
        self.guest_id = id
        self.guest_name = name
        self.number_of_days = days
        self.room_charge_per_day = charge
    def calculations(self):
        self.bill = self.number_of_days * self.room_charge_per_day
        self.gst = 0.12 * self.bill
        self.final_bill = self.bill + self.gst
    def display(self):
        print("---------Hatel Bill--------")
        print("Guest ID              : ",self.guest_id)
        print("Guest Name            : ",self.guest_name)
        print("Number OF Days        : ",self.number_of_days)
        print("Room charge per day   : ",self.room_charge_per_day)
        print("Room Bill             : ",self.bill)
        print("GST (12%)             : ",self.gst)
        print("Final Bill            : ",self.final_bill)

id = input("Enter Guset ID = ")
name = input("Enter Guest Name = ")
days = int(input("Enter Number OF days = "))
charge = int(input("Enter room charge per day = "))

obj = guest(id,name,days,charge)
obj.calculations()
obj.display()