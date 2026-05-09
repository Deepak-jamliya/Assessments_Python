'''
4. Reverse a Number
A security system stores OTP codes in reverse format for 
encryption to increase data safety. Reversing a number means 
extracting digits and rebuilding it in reverse order.
Write a program to *reverse a given integer using loops*.

Input: 1234
Output: 4321'''

# while loop
'''
num = int(input("Enter OTP : "))
while num > 0:
    rem = num % 10
    print(rem,end = "")
    num = num // 10'''

# for Loop:

num = int(input("Enter OTP : "))

for i in range(len(str(num))):
    digit = num % 10
    print(digit,end = "")
    num = num // 10