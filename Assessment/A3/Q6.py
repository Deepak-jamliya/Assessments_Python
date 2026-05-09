'''Assignment 6: Discount Calculator

Write a Python program that:

Accepts total amount.
Calculates 10% discount and final price.

Input:
Amount = 1000

Output:
Discount = 100
Final = 900
------------------------------------------------------------------------'''


total = int(input("Enter the total amount : "))
dis = total * 0.1

final = total - dis

print(f"Discount = {dis}\nFinal = {final}")


