'''

5. Palindrome Check
A number plate is considered special if it reads the same forward
and backward. Such numbers are called palindromes.
Write a program to *check whether a given number is a 
palindrome using loops*.

Input: 121
Output: Palindrome'''

# while loop
'''num = int(input("Number = "))
rev = 0
check = num

while num > 0:
    last = num % 10
    rev = rev * 10 + last
    num= num // 10

if check == rev:
    print("Palindrome")
else:
    print("Not a Palindrome")'''


# for loop

num = int(input("Enter Number = "))
temp = num
rev = 0

for i in range(len(str(num))):
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

if temp == rev:
    print("Palinndrome")
else:
    print("Not a Palindrome")
