'''Assignment 5: Average Marks Calculator

Write a Python program that:

Accepts marks of 3 subjects.
Calculates average.

Input:
Marks = 80, 90, 70

Output:
Average = 80.0
---------------------------------------------------------------------------'''


a,b,c = map(int,input("Enter marks of any three subjects : ").split())
avg = (a + b + c) / 3

print("Average : ",avg)