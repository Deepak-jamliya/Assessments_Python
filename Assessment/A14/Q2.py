'''
2. Multi Stage Prime Lock System

A smart locker opens only if final derived number is prime.

Write a program to:

- Find sum of digits
- Find product of digits
- Find difference between product and sum
- Count digits in difference
- Add digit count to difference
- Check whether final result is Prime or Not

Input:
234

Output:
Sum = 9
Product = 24
Difference = 15
Digits = 2
Final Result = 17
Prime'''

num = int(input("Enter Number = "))
sum = 0
product = 1
count = 0

while num > 0:
    digit = num % 10
    sum = sum + digit
    product = product * digit
    num = num // 10

print("Sum = ",sum)
print("Product = ",product)

diff = product - sum
odiff = diff
print("Difference = ",diff)

while diff > 0:
    digit = diff % 10
    count+=1
    diff = diff // 10
print("Digits = ",count)

final = odiff + count

print("Final Result = ",final)

i = 2
while i < final//2:
    if final%i == 0:
        print("Not Prime")
        break
    i+=1
else:
    print("Prime")