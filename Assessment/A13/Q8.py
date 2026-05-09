'''
8. Largest Smallest Sum Prime Checker

A number analyzer finds largest and smallest digit.

Write a program to:

- Find largest digit
- Find smallest digit
- Find sum of both
- Check whether sum is Prime or Not

Input:
57294

Output:
Largest = 9
Smallest = 2
Sum = 11
Prime'''

num = int(input("Enter Number = "))

largest = 0
smallest = 9

while num > 0:
    digit = num % 10
    if digit < smallest:
        smallest = digit
    if digit > largest:
        largest = digit
    num = num // 10
print("Largest = ",largest)
print("Smallest = ",smallest)

sum = largest + smallest
print("Sum = ",sum)

i = 2
prime = 1
while i <= sum//2:
    if sum%i == 0:
        prime = 0
        break
    i+=1

if prime:
    print("Prime")
else:
    print("Not Prime")


