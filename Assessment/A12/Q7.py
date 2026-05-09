'''
7. Duck Number Checker

A verification system is used by an e-commerce company to validate promotional coupon numbers.
Coupon numbers containing at least one zero in between digits are considered special duck numbers.
However, if the number starts with zero, it is rejected immediately.

A duck number is a number that contains at least one zero but does not start with zero.

Example:
1023

Write a program using loops to check whether the entered number is a Duck number.

Input:
1023

Output:
Duck Number'''

# while loop
'''num = input("Enter Number = ")
zero = False

if  num[0] == '0':
    print("Not a duck number")
else:
    num = int(num)
    while num > 0:
        digit = num % 10
        if digit == 0:
            zero = True
            break
        num = num // 10
    if zero:
        print("Duck number")
    else:
        print("Not a duck number")'''

# for loop
num = input("Enter Number = ")

if num[0] == 0:
    print("Not a duck Number")

else:
    num = int(num)
    for i in range(len(str(num))):
        digit = num % 10
        if digit == 0:
            print("Duck Number")
            break
        num = num // 10
    else:
        print("Not a duck Number")
    