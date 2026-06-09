'''
=====================================================================
QUESTION 4: ONLINE SHOPPING ORDERS
==================================

An online shopping company stores customer orders using NamedTuple.

Fields:
order_id, customer_name, product_name, amount

Requirements:

1. Read N order records from the user and store them in a list of NamedTuples.

---

2. Display all order details.

---

3. Find and display the order having the highest amount.

---

4. Calculate and display total sales.

---

5. Count the number of orders whose amount is greater than ₹10,000.

---

Test Case:

Input:
Enter number of orders: 5

O101 Rahul Laptop 55000
O102 Priya Mouse 800
O103 Amit Mobile 25000
O104 Neha Keyboard 1500
O105 Rakesh TV 45000

Expected Output:
Highest Value Order:
O101 Rahul Laptop 55000

Total Sales:
127300

Orders Above ₹10,000:
3
'''

from collections import namedtuple
n = int(input("Enter Number of Orders = "))

orders = namedtuple("orders",["order_id", "customer_name", "product_name", "amount"])

data = []

for i in range(n):
    o = input(f"Enter order {i+1} id = ")
    c = input(f"Enter Customer {i+1} name = ")
    p = input(f"Enter Product {i+1} name = ")
    a = int(input(f"Enter Product {i+1} Price = "))
    data.append(orders(o,c,p,a))

print("\nOrder Details:")
for i in data:
    print(i.order_id, i.customer_name, i.product_name, i.amount)

highest = data[0].amount
high = data[0]
total = 0
count = 0

for i in data:
    if i.amount > highest:
        highest = i.amount
        high = i
    total+=i.amount
    if i.amount > 10000:
        count+=1
print("\nHighest Value Order : \n")
print(high.order_id, high.customer_name, high.product_name, high.amount)
print("\nTotal Sales :\n",total)
print("\nOrders Above 10000:")
print(count)



