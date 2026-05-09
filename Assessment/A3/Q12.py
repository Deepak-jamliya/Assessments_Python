'''Assignment 12: Change Return System

Write a Python program that:

Accepts amount.
Calculates ₹100, ₹50, ₹10 notes.

Input:
Amount = 380

Output:
₹100 x 3
₹50 x 1
₹10 x 3
-----------------------------------------------------------------------------------------'''

amount = int(input("Enter the amount : "))
hun = amount // 100
remain = amount % 100

fifty = remain // 50
remain = remain  % 50

ten = remain // 10

print(f"₹100 x {hun}\n₹50 x {fifty}\n₹10 x {ten}")