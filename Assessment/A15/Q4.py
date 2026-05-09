'''
4.Spy Number Detector

A cybersecurity system flags special numeric codes.

A number is called a Spy Number if:
Sum of digits = Product of digits

Write a program to check whether the entered number is Spy Number or Not.

Input:
1124

Output:
Spy Number'''

n = int(input("Enter Number = "))
sum = 0
product = 1

while n > 0:
    digit = n % 10
    sum = sum + digit
    product = product * digit
    n = n // 10

if sum == product:
    print("Spy number")
else:
    print("Not a spy Number")
