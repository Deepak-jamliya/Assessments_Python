'''Assignment 1: Restaurant Bill Split

A group of friends went to a restaurant. The restaurant adds GST and service charge to the bill, and then the total is divided equally.

Input:
Total bill amount = 2500
GST = 5%
Service charge = 10%
Number of friends = 4

Expected Output:
Final Bill = 2875.0
Each Person Pays = 718.75
------------------------------------------------------------------------------------------------------------------------------'''


bill = int(input("Enter the total bill amount : "))
Gst = int(input("Enter GST : "))
service = int(input("Enter service charge : "))
count = int(input("Enter number of friends : "))

GSTbill = bill * (5/100)
sbill = bill * 0.1
total = bill + GSTbill + sbill
split = total / count

print(f"Final Bill = {total}\nEach person pays = {split}")