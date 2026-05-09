'''
Even Odd Difference Prime System

A smart scanner counts even and odd digits.

Write a program to:

- Count even digits
- Count odd digits
- Find difference
- Check whether difference is Prime or Not

Input:
123456

Output:
Even Count = 3
Odd Count = 3
Difference = 0
Not Prime'''

num = int(input("Enter Number = "))
even_count = 0
odd_count = 0

while num > 0:
    digit = num % 10
    if digit%2 == 0:
        even_count+=1
    else:
        odd_count+=1
    num = num // 10

print("Even Count = ",even_count)
print("Odd Count = ",odd_count)

diff = even_count - odd_count
print("Difference = ",diff)

if diff <= 1:
    print("Not Prime")

else:
    i = 2
    prime = 1
    while i <= diff//2:
        if diff%i == 0:
            prime = 0
            break
        i+=1
    if prime:
        print("Prime")
    else:
        print("Not Prime")