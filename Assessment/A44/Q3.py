'''
Question 3: Online Shopping System
Scenario

An e-commerce company wants to calculate the final amount payable by customers after applying 
discounts.

Requirements

Create a class named Product with:

product_id
product_name
quantity
price_per_item

Initialize the values using a constructor.

Calculations
Total Amount = Quantity × Price Per Item
If Total Amount > ₹5000, Discount = 10%
Otherwise, Discount = 5%
Final Amount = Total Amount − Discount
Sample Input
Enter Product ID : P101
Enter Product Name : Laptop
Enter Quantity : 2
Enter Price Per Item : 35000
Sample Output
------ Shopping Bill ------
Product ID        : P101
Product Name      : Laptop
Quantity          : 2
Price Per Item    : 35000.0
Total Amount      : ₹70000.0
Discount          : ₹7000.0
Final Amount      : ₹63000.0
'''

class Product:
    def __init__(self,id,name,quantity,price):
        self.product_id = id
        self.product_name = name
        self.quantity = quantity
        self.price_per_item = price
    def calculations(self):
        self.total = self.quantity * self.price_per_item
        if self.total > 5000:
            self.dis = 0.1 * self.total
            self.final = self.total - self.dis
        else:
            self.dis = 0.05 * self.total
            self.final = self.total - self.dis
    def display(self):
        print("----- Shopping Bill ----")
        print("Product ID        : ",self.product_id)
        print("Product Name      : ",self.product_name)
        print("Quantity          : ",self.quantity)
        print("Price Per Item    : ",self.price_per_item)
        print("Total Amount      : ",self.total)
        print("Discount          : ",self.dis)
        print("Final Amount      : ",self.final)
id = input("Enter Product ID = ")
name = input("Enter Product Name = ")
quantity = int(input("Enter Quantity = "))
price = float(input("Enter Price per Item = "))

obj = Product(id,name,quantity,price)
obj.calculations()
obj.display()


