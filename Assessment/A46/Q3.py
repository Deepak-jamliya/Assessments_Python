'''
ASSIGNMENT 3: Online Shopping System (Hierarchical Inheritance)
Scenario
An e-commerce company sells multiple categories of products.
Create a base class Product.
Common Details
Product ID
Product Name
Price
Derived Classes
Electronics
Brand
Warranty
Clothing
Size
Fabric Type
Grocery
Expiry Date
Weight
Functional Requirements
========== Online Shopping ==========
1. Add Electronics Product
2. Add Clothing Product
3. Add Grocery Product
4. Display Electronics
5. Display Clothing
6. Display Grocery
7. Exit
Sample Input
Choice : 1

Product ID : 501
Product Name : Laptop
Price : 65000

Brand : Dell
Warranty : 2 Years
Sample Output
Electronics Product

Product ID : 501
Product Name : Laptop
Brand : Dell
Warranty : 2 Years
Price : ₹65000
'''

class Product:
    def __init__(self,product_id,product_name,price):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
    def display_product(self):
        print("Product ID = ",self.product_id)
        print("Product Name = ",self.product_name)
        print("Product Price = ",self.price)
class Electronics(Product):
    def __init__(self,product_id,product_name,price,brand,warranty):
        super().__init__(product_id,product_name,price)
        self.brand = brand
        self.warranty = warranty
    def display_electronics(self):
        print("========== Electronics =======")
        self.display_product()
        print("Brand = ",self.brand)
        print("Warranty = ",self.warranty)
class Clothing(Product):
    def __init__(self, product_id, product_name, price, size, fabric_type):
        super().__init__(product_id, product_name, price)
        self.size = size
        self.fabric_type = fabric_type
    def display_cloth(self):
        print("========== Clothing =======")
        self.display_product()
        print("Brand = ",self.size)
        print("Warranty = ",self.fabric_type)
class Grocery(Product):
    def __init__(self, product_id, product_name, price, expiry_date, weight):
        super().__init__(product_id, product_name, price)
        self.expiry_date = expiry_date
        self.weight = weight
    def display_grocery(self):
        print("========== Grocery =======")
        self.display_product()
        print("Brand = ",self.expiry_date)
        print("Warranty = ",self.weight)

while True:
    print("========= Online Shopping ========")
    print("1. Add Electronics Product")
    print("2. Add Clothing Product")
    print("3. Add Grocery Product")
    print("4. Display Electronics")
    print("5. Display Clothing")
    print("6. Display Grocery")
    print("7. Exit")

    choice = int(input("Enter Your Choice = "))
    match choice:
        case 1:
            product_id = int(input("Enter Product ID = "))
            product_name = input("Enter Product Name = ")
            price = float(input("Enter Product Price = "))
            brand = input("Enter Product Brand = ")
            warranty = int(input("Enter Warranty = "))
            elec = Electronics(product_id,product_name,price,brand,warranty)
            print("Item Added Successfully")
        case 2:
            product_id = int(input("Enter Product ID = "))
            product_name = input("Enter Product Name = ")
            price = float(input("Enter Product Price = "))
            size = input("Enter Cloth Size = ")
            fabric_type = int(input("Enter Fabric Type = "))
            cloth = Clothing(product_id,product_name,price,size,fabric_type)
            print("Item Added Successfully")
        case 3:
            product_id = int(input("Enter Product ID = "))
            product_name = input("Enter Product Name = ")
            price = float(input("Enter Product Price = "))
            expiry_date = input("Enter Expiry Date = ")
            weight = int(input("Enter Weight = "))
            grocery = Grocery(product_id,product_name,price,brand,warranty)
            print("Item Added Successfully")
        case 4:
            elec.display_electronics()
        case 5:
            cloth.display_cloth()
        case 6:
            grocery.display_grocery()
        case 7:
            print("Thank you For using This System")
            break
        case _:
            print("Invalid Choice")
