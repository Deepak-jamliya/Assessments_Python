'''
ASSIGNMENT 4: Banking Loan Management System (Multilevel Inheritance)
Scenario
A bank wants software for loan management.
Class Hierarchy
Person
     ↓
Customer
     ↓
LoanAccount
Person
Name
Age
Mobile Number
Customer
Customer ID
Account Number
LoanAccount
Loan Amount
Interest Rate
Loan Tenure
Functional Requirements
Add Customer Loan Details
Display Loan Details
Exit
Sample Input
Customer Name : Ajay Singh
Age : 36
Mobile : 9999999999

Customer ID : C101
Account Number : 100245785

Loan Amount : 500000
Interest Rate : 8.5
Loan Tenure : 5
Sample Output
----------- Loan Details -----------

Customer Name : Ajay Singh
Customer ID : C101
Account Number : 100245785

Loan Amount : ₹500000
Interest Rate : 8.5%
Loan Tenure : 5 Years
'''

class Person:
    def __init__(self,name,age,mob):
        self.name = name
        self.age = age
        self.mob = mob
    
class Customer(Person):
    def __init__(self, name, age, mob, customer_id, acc_no):
        super().__init__(name, age, mob)
        self.customer_id = customer_id
        self.acc_no = acc_no
    def display_customer(self):
        print("Customer Name = ",self.name)
        print("Customer ID = ",self.customer_id)
        print("Account Number = ",self.acc_no)

class LoanAccount(Customer):
    def __init__(self, name, age, mob, customer_id, acc_no, loan_amount, interest, tenure):
        super().__init__(name, age, mob, customer_id, acc_no)
        self.loan_amount = loan_amount
        self.interest = interest
        self.tenure = tenure
    def display_details(self):
        print("======== Loan Details ======")
        self.display_customer()
        print("Loan Amount = ",self.loan_amount)
        print("Interest Rate = ",self.interest)
        print("Tenure = ",self.tenure)


while True:
    print("1. Add Cutsomer Loan Details")
    print("2. Display Loan Details")
    print("3. Exit")

    choice = int(input("Enter Choice = "))
    match choice:
        case 1:
            name = input("Enter Customer Name = ")
            age = int(input("Enter Customer Age = "))
            mob = int(input("Enter Mob Number = "))
            customer_id = input("Enter Customer ID = ")
            acc_no = int(input("Enter Account Number  = "))
            loan_amount = float(input("Enter Loan Amount = "))
            interest = float(input("Enter Interest Rate = "))
            tenure = int(input("Enter Tenure = "))
            loan = LoanAccount(name,age,mob,customer_id,acc_no,loan_amount,interest,tenure)
            print("Details Added Successfully")
        case 2:
            loan.display_details()
        case 3:
            print("Thank You")
            break
        case _:
            print("Invalid Choice")
