'''Write a Python program that:

Accepts distance (in km) and time (in hours).
Calculates speed.

Input:
Distance = 120
Time = 2

Output:
Speed = 60 km/h
----------------------------------------------------------------'''



dis = int(input("Enter total distance covered in Km :  "))
time = int(input("Enter the total time taken in hrs : "))
S = dis/time

print("Speed : {}km/h".format(S))
