'''Assignment 14: Simple Profit or Loss Calculator

Write a Python program that:

Accepts cost price and selling price.
Calculates profit/loss and percentage.

Input:
Cost Price = 1000
Selling Price = 1200

Output:
Profit = 200
Profit % = 20.0
-------------------------------------------------------------------------'''

cp,sp = map(int,input("Enter cost price and selling price : ").split())

if(sp>cp):
  result = sp - cp
  pper = (result/cp)*100
  print(f"Profit = {result}\nProfit% = {pper}")

else:
  result = cp - sp
  lper = (result/cp)*100
  print(f"Loss = {result}\nLoss% = {lper}")



