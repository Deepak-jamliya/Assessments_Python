'''Assignment 11: Time Duration Adder

Write a Python program that:

Accepts hours, minutes, seconds.
Converts into total seconds.

Input:
Hours = 1
Minutes = 2
Seconds = 30

Output:
Total Seconds = 3750
---------------------------------------------------------------------------------'''

hrs,min,sec = map(int,input("Enter duration as hours, minutes and seconds : ").split())
fhrs = hrs * 3600
fmin = min * 60

fsec = fhrs + fmin + sec

print("Total Seconds = ",fsec) 