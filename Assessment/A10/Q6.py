'''
6. Armstrong Number (3-digit)
In coding competitions, certain numbers are considered unique. A 3-digit Armstrong number
 is one where the sum of the cubes of its digits equals the number itself.
Write a program to *check whether a number is an Armstrong number using loops*.

Input: 153
Output: Armstrong'''

# while loop
'''num = int(input("Enter Number = "))
check = num
sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit**3
    num = num // 10

if check == sum:
    print("Armstrong")
else:
    print("Not an Armstrong number")'''


# for loop

num = int(input("Enter Number = "))
sum = 0
temp = num

for i in range(len(str(num))):
    digit = num % 10
    sum = sum + digit**3
    num = num // 10

if temp == sum:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

    