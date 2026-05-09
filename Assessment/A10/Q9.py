'''
 Check All Digits Are Even*
A machine only accepts numbers where every digit is even. If any digit is odd, the number is rejected.
Write a program to *check whether all digits of a number are even using loops*.

Input: 2468
Output: All Even

Input: 2456
Output: Not All Even'''

# while loop
'''num = int(input("Enter number : "))
check = 1

while num > 0:
    digit = num % 10
    if digit %2 != 0:
        check = 0
        break
    num = num // 10

if check == 1:
    print("All Are Even")
else:
    print("Not all even")'''

# for loop
num = int(input("Enter Number = "))

for i in range(len(str(num))):
    digit = num % 10
    if digit%2 != 0:
        print("All Numbers are not even")
        break
    num = num // 10
else:
    print("All Number are even")

