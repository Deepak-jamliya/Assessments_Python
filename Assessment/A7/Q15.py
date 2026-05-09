'''
15. Smart Parking System

A smart parking system charges based on vehicle type and parking duration:

* Bike → ₹10/hour
* Car → ₹20/hour
* Bus → ₹50/hour
  If parking duration exceeds 5 hours, an additional ₹100 penalty is applied.

Write a Python program to calculate total parking fee.

Input:
Enter vehicle type: Car
Enter hours parked: 6

Output:
Total Parking Fee: ₹220
------------------------------------------------------------------------------------------'''

type = input("Enter Vehicle type : ")
time = int(input("Enter hours parked : "))

if type == "bike":
  fee = 10 * time
elif type == "car":
  fee = 20 * time
elif type == "bus":
  fee = 50 * time
else:
  print("Invalid Choice")

if time > 5:
  fee = fee + 100

print("Total Parking Fee = ",fee)