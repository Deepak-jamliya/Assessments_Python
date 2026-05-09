'''
1. Triple Operation Prime Verification System

A cybersecurity company generates a security score from entered access code.

Write a program to:

- Find sum of digits of the number
- Reverse the number
- Find absolute difference between original number and reverse
- Add digit sum and difference
- Check whether final result is Prime or Not Prime

Input:
4215

Output:
Sum of Digits = 12
Reverse = 5124
Difference = 909
Final Result = 921
Not Prime'''

num = int(input("Enter Number = "))
temp = num
sum = 0
rev = 0

while num > 0:
    digit = num % 10
    sum = sum + digit
    rev = rev * 10 + digit
    num = num // 10

print("Sum of Digits = ",sum)
print("Reverse = ",rev)

diff = abs(rev - temp)
print("Difference = ",diff)

final = sum + diff
print("Final Number = ",final)


for i in range(2,final//2+1):
    if final%i == 0:
        print("Not Prime")
        break
else:
    print("Not Prime")
