'''Assignment 10: Percentage Calculator

Write a Python program that:

Accepts total marks and obtained marks.
Calculates percentage.

Input:
Total = 500
Obtained = 400

Output:
Percentage = 80%
-----------------------------------------------------------------------------'''

total = int(input("Enter total number of marks : "))
obtained = int(input("Enter marks obtained : "))

percentage = (obtained/total)*100

print("Percentage : {}%".format(percentage))