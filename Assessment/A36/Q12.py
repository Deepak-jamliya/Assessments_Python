'''
12.

=========================================
ONLINE FOOD DELIVERY ANALYSIS
=============================

orders = [
"Pizza",
"Burger",
"Pizza",
"Pasta",
"Burger",
"Pizza",
"Pasta"
]

Write a program to:

* Count orders of each food item.
* Find the most ordered item.

Sample Output:
Pizza : 3
Burger : 2
Pasta : 2

Most Ordered : Pizza
'''

orders = ["Pizza","Burger","Pizza","Pasta","Burger","Pizza","Pasta"]

d = {}

for i in orders:
    count = 0
    for j in orders:
        if i == j:
            count+=1
    d[i] = count

max = max(d,key = d.get)
print(d)
print("Most Ordered = ",max)
