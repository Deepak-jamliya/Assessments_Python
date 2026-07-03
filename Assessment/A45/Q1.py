'''
QNO 1: Bank Account Management System

ABC Bank wants to develop a software application to manage customer accounts.

Each customer has:

Account Number
Customer Name
Account Balance

A customer should be able to:

Deposit money
Withdraw money
Check account balance
Transfer money to another customer

The bank also wants to maintain information that is common for all customers:

Bank Name
Interest Rate

The bank management may change the interest rate in the future, and the change should apply to 
all customers.

Additionally, the application should provide some utility operations:

Validate whether an account number is valid.
Calculate interest on a given amount.
Generate a transaction ID.
Requirements

Class Variables

bank_name
interest_rate

Instance Variables

account_no
customer_name
balance

Instance Methods

deposit(amount)
withdraw(amount)
transfer_money(receiver, amount)
display_balance()

Class Methods

change_interest_rate(new_rate)
change_bank_name(new_name)
display_bank_info()

Static Methods

validate_account_number(account_no)
calculate_interest(amount, rate)
generate_transaction_id()

Sample Input
Customer 1
Account No : 1001
Name       : deepika
Balance    : 50000

Customer 2
Account No : 1002
Name       : Priya
Balance    : 30000

Deposit Amount : 10000
Transfer Amount : 15000
New Interest Rate : 7.5
Sample Output
Customer : deepika
Balance  : 45000

Customer : Priya
Balance  : 45000

Bank Name      : ABC Bank
Interest Rate  : 7.5%
Transaction ID : TXN1025

Task: Design a Python class named BankAccount and implement all the above methods using instance 
methods, class methods, and static methods appropriately.
'''

import random

class BankAccount:
    bank_name = "ABC Bank"
    interest_rate = 5.0

    def __init__(self, account_no, customer_name, balance):
        self.account_no = account_no
        self.customer_name = customer_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient Balance")

    def transfer_money(self, receiver, amount):
        if amount <= self.balance:
            self.balance -= amount
            receiver.balance += amount
        else:
            print("Insufficient Balance for Transfer")

    def display_balance(self):
        print(f"Customer : {self.customer_name}")
        print(f"Balance  : {self.balance}")

    @classmethod
    def change_interest_rate(cls, new_rate):
        cls.interest_rate = new_rate

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name

    @classmethod
    def display_bank_info(cls):
        print(f"Bank Name      : {cls.bank_name}")
        print(f"Interest Rate  : {cls.interest_rate}%")

    @staticmethod
    def validate_account_number(account_no):
        return len(str(account_no)) == 4

    @staticmethod
    def calculate_interest(amount, rate):
        return (amount * rate) / 100

    @staticmethod
    def generate_transaction_id():
        return "TXN" + str(random.randint(1000, 9999))


acc1 = int(input("Enter Account Number for Customer 1: "))
name1 = input("Enter Name for Customer 1: ")
bal1 = int(input("Enter Balance for Customer 1: "))

acc2 = int(input("Enter Account Number for Customer 2: "))
name2 = input("Enter Name for Customer 2: ")
bal2 = int(input("Enter Balance for Customer 2: "))

deposit_amount = int(input("Enter Deposit Amount: "))
transfer_amount = int(input("Enter Transfer Amount: "))
new_interest_rate = float(input("Enter New Interest Rate: "))


cust1 = BankAccount(acc1, name1, bal1)
cust2 = BankAccount(acc2, name2, bal2)


cust1.deposit(deposit_amount)
cust1.transfer_money(cust2, transfer_amount)

BankAccount.change_interest_rate(new_interest_rate)

cust1.display_balance()
cust2.display_balance()

BankAccount.display_bank_info()
print("Transaction ID :", BankAccount.generate_transaction_id())