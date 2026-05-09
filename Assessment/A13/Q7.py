'''
 Prime Sum Lucky Number

A lottery app checks if sum of digits is prime.

Write a program to:

- Find sum of digits
- If prime print Lucky Number
- Else Normal Number

Input:
4528

Output:
Sum = 19
Lucky Number'''

num = int(input("Enter Number = "))

sum = 0
while num > 0:
    digit = num % 10
    sum = sum + digit
    num = num // 10
print(sum)
i = 2
is_prime = 1
while i <= sum//2:
    if sum%i == 0:
        is_prime = 0
        break
    i+=1

if is_prime:
    print("Lucky Number")
else:
    print("Normal Number")