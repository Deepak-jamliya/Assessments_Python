'''
6.

NOTE: using tuple only
An electronics store wants to maintain product information. Since product details should not be modified accidentally,
 each product record is stored as a tuple.

Tuple Format:

(product_id, product_name, price)

Requirements:

Read N product details from the user and store them as tuples in a list.
Display all product details.
Find and display the costliest product.
Find and display the cheapest product.
Calculate and display the average price of all products.
Display all products whose price is greater than ₹50,000.

Test Case:

Input:

Enter number of products: 4

P101 Laptop 65000
P102 Mobile 25000
P103 Television 80000
P104 Tablet 30000

Expected Output:

All Products:
('P101', 'Laptop', 65000)
('P102', 'Mobile', 25000)
('P103', 'Television', 80000)
('P104', 'Tablet', 30000)

Costliest Product:
('P103', 'Television', 80000)

Cheapest Product:
('P102', 'Mobile', 25000)

Average Price:
50000.0

Products Above ₹50,000:
('P101', 'Laptop', 65000)
('P103', 'Television', 80000)
'''

from collections import namedtuple

n = int(input("Enter Number of products = "))

details = namedtuple("details",["product_id", "product_name", "price"])
data = []

for i in range(n):
    id = input(f"Enter Product {i+1} id = ")
    n = input(f"Enter Product {i+1} name = ")
    p = int(input(f"Enter Book {i+1} Price = "))
    data.append(details(id,n,p))

print("\nProduct Details : ")
for i in data:
    print(i.product_id, i.product_name, i.price)

cost = data[0]
c = data[0].price
cheap = data[0]
che = data[0].price
sum = 0

for i in data:
    if i.price > c:
        c = i.price
        cost = i
    if i.price < che:
        che = i.price
        cheap = i
    sum+=i.price

print("\nCostliest Product:")
print(cost.product_id, cost.product_name, cost.price)
print("\nCheapest Prroduct : ")
print(cheap.product_id, cheap.product_name, cheap.price)
print("\nAverage Price : ")
print(sum/len(data))

print("\nProducts Above ₹50,000 : ")
for i in data:
    if i.price > 50000:
        print(i.product_id, i.product_name, i.price)




