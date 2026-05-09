'''
7.
 Alternate Digit Prime Checker

A math lab adds alternate digits from right side.

Write a program to:

- Find sum of alternate digits
- Check whether sum is Prime or Not

Input:
12345

Output:
Alternate Sum = 9
Not Prime'''

num = int(input("Enter Number = "))
sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit
    num = num // 10
    num = num // 10
print("Alternate Sum = ",sum)

for i in range(2,sum//2+1):
    if sum%i == 0:
        print("Not Prime")
        break
else:
    print("Prime")