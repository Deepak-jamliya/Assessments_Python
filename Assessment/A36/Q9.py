'''
9.
=========================================
INVENTORY MANAGEMENT SYSTEM
===========================

Store product stock in a dictionary.

stock = {
"Pen":50,
"Pencil":100,
"Eraser":25,
"Marker":10
}

Write a program to:

* Display products having stock less than 30.

Sample Output:
Eraser
Marker
'''

n = int(input("Enter Number of items = "))
d = {}

for i in range(n):
    key = input(f"Enter Item {i+1} name = ")
    v = int(input(f"Enter Quantity of item {i+1} = "))
    d[key] = v

for k,v in d.items():
    if v < 30:
        print(k)