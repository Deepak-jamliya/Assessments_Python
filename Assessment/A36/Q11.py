'''
11.
=========================================
PRODUCT SALES ANALYSIS
======================

sales = [
"Mobile",
"Laptop",
"Mobile",
"Tablet",
"Laptop",
"Mobile"
]

Write a program to:

* Count sales of each product.
* Display products in sorted order.

Sample Output:
Laptop : 2
Mobile : 3
Tablet : 1
'''

sales = ["Mobile","Laptop","Mobile","Tablet","Laptop","Mobile"]
d = {}

for i in sales:
    count = 0
    for j in sales:
        if i == j:
            count+=1
    d[i] = count
for k,v in sorted(d.items()):
    print(k,":",v)
