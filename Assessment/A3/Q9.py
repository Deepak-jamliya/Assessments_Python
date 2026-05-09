'''Assignment 9: Fuel Cost Calculator

Write a Python program that:

Accepts distance (km), mileage (km/litre), and petrol price.
Calculates total fuel cost.

Input:
Distance = 100
Mileage = 20
Petrol Price = 100

Output:
Cost = 500
--------------------------------------------------------------------------------------'''

dis = int(input("Enter distance(km): "))
mil = int(input("Enter mileage(km/l) : "))
fuel = int(input("Enter petrol price : "))
cost = (dis/mil)*fuel

print("Cost : ",cost)
