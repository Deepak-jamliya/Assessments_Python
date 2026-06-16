'''
1.

=========================================
ONLINE SHOPPING CART
====================

A shopping website stores purchased products in a dictionary where:
Key = Product Name
Value = Quantity Purchased

Write a program to:

* Accept a dictionary from the user.
* Calculate and display the total quantity of products purchased.

Sample Input:
{"Laptop":2,"Mouse":3,"Keyboard":1}

Sample Output:
Total Quantity = 6
'''

n = int(input("Enter Number of Items = "))
products = {}

for i in range(n):
    key = input(f"Enter Product {i+1} name = ")
    v = int(input("Enter Quantity of the product = "))
    products[key] = v

total = 0

for i,j in products.items():
    total+=j

print("\nTotal Quantity = ",total)
