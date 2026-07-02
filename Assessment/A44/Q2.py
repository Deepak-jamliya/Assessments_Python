'''
Question 2: Electricity Bill Calculator
Scenario

An electricity company wants to generate monthly bills for its customers.

Requirements

Create a class named Customer with:

customer_id
customer_name
units_consumed

Initialize the values using a constructor.

Calculations
Cost per Unit = ₹8
Fixed Charge = ₹150
Total Bill = (Units × 8) + 150
Sample Input
Enter Customer ID : C101
Enter Customer Name : Amit Verma
Enter Units Consumed : 350
Sample Output
------ Electricity Bill ------
Customer ID       : C101
Customer Name     : Amit Verma
Units Consumed    : 350
Total Bill Amount : ₹2950.0
'''

class Customer:
    def __init__(self,id,name,units):
        self.customer_id = id
        self.customer_name = name
        self.units_consumed = units
    def calculations(self):
        self.total_bill = (self.units_consumed * 8) + 150
    def display(self):
        print("-------- Electricity Bill --------")
        print("Customer ID         : ",self.customer_id)
        print("Customer Name       : ",self.customer_name)
        print("Total Bill Amount   : ",self.total_bill)

id = input("Enter Customer ID = ")
name = input("Enter Customer Name = ")
units = float(input("Enter Units Consumed = "))

obj = Customer(id,name,units)
obj.calculations()
obj.display()
