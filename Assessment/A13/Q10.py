'''
Zero Count Prime Scanner

A banking system checks account numbers.

Write a program to:

- Count zero digits
- Find sum of digits
- Add zero count and sum
- Multiply by smallest digit
- Check whether final result is Prime or Not

Input:
908406

Output:
Zero Count = 2
Sum = 27
Smallest Digit = 0
Final Result = 0
Not Prime'''

num = int(input("Enter Number = "))
temp = num
count = 0
sum = 0
smallest = 9

while num > 0:
    digit = num % 10
    if digit == 0:
        count+=1
    if digit < smallest:
        smallest = digit
    sum = sum + digit
    num = num // 10

print("Zero Count = ",count)
print("Sum = ",sum)
print("Smallest = ",smallest)

