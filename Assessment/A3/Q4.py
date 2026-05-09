'''Assignment 4: Area of Rectangle

Write a Python program that:

Accepts length and breadth.
Calculates area.

Input:
Length = 10
Breadth = 5

Output:
Area = 50
----------------------------------------------------------------------'''


l,b = map(int,input("Enter length and breadth : ").split())
area = l * b

print("Area of Rectangle : ",area)