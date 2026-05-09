'''Assignment 2: Mobile EMI Calculation

You purchased a mobile phone using EMI. After paying a down payment, the remaining amount includes interest and is divided into monthly installments.

Input:
Mobile price = 30000
Down payment = 5000
Interest rate = 10%
Months = 10

Expected Output:
Remaining Amount = 25000
Total with Interest = 27500
Monthly EMI = 2750.0
-----------------------------------------------------------------------------------------------------------'''


price = int(input("Enter the price of mobile : "))
dpay = int(input("Enter down payment amount : "))
interest = int(input("Enter interest rate : "))
month = int(input("Enter number of months : "))

ramount = price - dpay
intamount = (ramount * interest)/100
total = ramount + intamount
emi = total / month

print(f"Remaining amount = {ramount}\nTotal with interest = {total}\nMonthly EMI = {emi}")

